# c 语言实现协程  
[英文原版](https://www.chiark.greenend.org.uk/~sgtatham/coroutines.html)  
*by [Simon Tatham](http://pobox.com/~anakin/)*  

## 简介  
通常，构建大型程序是一件很困难的事情。此处展示一个经常遇到的问题：*如果，你写了一段代码用于产生数据，另一段代码用于消费产生的数据，那么应该让谁调用谁呢？*
> 此处自然联想到了`生产者-消费者模型`：创建两个线程和一个队列，一个用于产生数据，另一个用于消费数据，二者不能同时操作队列(锁)  

下面是一段非常简单的，行程解压代码和解析代码：  
```c
/* 解压代码 */
while(1){
    c = getchar();
    if (c == EOF){
        break;
    }else{
        len = getchar();
        c = getchar();
        while(len--){
            emit(c);
        }
    }
    emit(EOF);
}

/* 解析代码 */
while(1){
    c = getchar();
    if(c == EOF){
        break;
    }
    if(isalpha(c)){
        do{
            add_to_token(c);
            c = getchar();
        } while (isalpha(c));
        got_token(WORD);
    }
    add_to_token(c);
    got_token(PUNCT);
}
```  
两段代码都很简单：一个在调用`emit()` 的时候产生字符数据;另一个通过`getchar()` 消费数据。如果只要在调用`emit()` 和`getchar()` 的时候，程序就互相给对方发送数据，那就可以简单地将两段代码`串联`，就可以实现解压(器)的输出直接送至解析(器)。  
在许多现代操作系统中，我们可以通过进(线)程间的`管道`(pipes) 进行通信。`emit()` 向管道中放数据，`getchar()` 从管道中获取数据，简单粗暴，但是太重了(*需要开辟线程，保存堆栈信息*)，对于这么简单的任务，就属于杀鸡用牛刀了。  
所以在本文中，我们会看到针对此类问题的一种非常有创造性的解决方案。  

## 重写  
一般我们会重写通信的其中一端(*就是任意一段代码*)，使其可以被调用。如下：  
```c  
/* 解压器 */
int decompressor(void){
    // 静态变量，用于保存现场
    static int repchar;
    static int replen;
    
    if(replen > 0){
        replen --;
        return repchar;
    }
    c = getchar();
    if(c == EOF){
        return EOF;
    }
    if(c == 0xFF){
        replen = getchar();
        repchar = getchar();
        replen--;
        return repchar;
    }else{
        return c;
    }
}

/* 解析器 */
void parser(int c){
    static enum{
        START,
        IN_WORD
    } state;

    switch(state){
        case IN_WORD:
            if(isalpha(c)){
                add_to_token(c);
                return;
            }
            got_token(WORD);
            state = START;
            // 跌落
        case START:
            add_to_token(c);
            if(isalpha(c)){
                state = IN_WORD;
            }else{
                got_token(PUNCT);
            }
            break;
    }
}
```  
两段代码只需重写一个就行：如果重写了解压器，每次调用就会返回一个字符，解析器就可以用`decompressor()` 函数替换掉`getchar()`，这样每次解析器需要字符时就会调用解压器生产字符，皆大欢喜(*类似于轮询，但是函数间的跳转会涉及到大量的栈操作，还是比较重*)。麻瓜才会两个都重写~  
另外，被调用者不好看呀(*作者这么个意思，我觉得挺清晰的啊*)  

## Knuth's coroutines  
在《计算机编程艺术》一书中，Donald Knuth 展示了一种解决方案：**完全抛弃了栈的概念**。没有调用者，也没有被调用者，只考虑二者的合作关系。

> 因为`call` 一个方法时，需要将其参数与返回值进行压栈/出栈操作，所以采取一种更轻量化的`call`：在汇编层面上指定返回值的地址，然后利用`jmp`替代`call`，这样便省去了栈操作。但是 ***不可移植***  

## 基于栈的协程