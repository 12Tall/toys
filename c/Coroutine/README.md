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
所以嘞，接受现实吧：在C 语言层面上，只能由一个函数调用另一个函数，调用者很容易实现，但是要实现被调用者`return` 后还能继续执行就不容易了(*从函数`retrun` ~~再次被调用时还能保存上一次的运行状态。似乎也不难啊，`static` 变量不行嘛~~ 后还能接着执行*)，如下代码：  
```c  
int function(void){
    int i;
    for(i=0;i<10;i++){
        return i;  // 当然不会成功，否则就活见鬼了
    }
}

// 利用goto 实现
int function(void){
    static int i, state = 0;
    switch(state){
        case 0: goto LABEL0;
        case 1: goto LABEL1;
    }
    LABEL0:  // 标签0
        for(i=0;i<10;i++){
            state = 1;
            return 1;
            LABEL1:;  // 标签1
            // 再次调用时就会通过switch 直接跳转到LABEL1
        }
}
/**
* 虽然有很多标签，但确实可以运行~~~ 
* 就……想起了一个段子
* C++：你造了一匹马，它很丑，而且看起来摇摇欲坠，但能干活。
* Java：你非常想造一匹马，但首先，你需要造一个马厩。
* JavaScript：你凑齐了所有造马需要的部件（框架），但马的骨架中多出了一个角（Angular），它瘫痪了。
* NoSQL？？？：你已经有了一匹又快又漂亮的马，但你不知道它到底在哪。
* COBOL：你 1962 年就造好了这匹马，但它只能被创造者驯服，对其他人来说，它是条龙。
* LISP：不解释……
* C#：这匹马伪装成骆驼时表现极好，但当你把它当马用时，它变得很挑剔（难伺候）。
* Assembly：虽然这匹马看起来很低级，但它也能跑(而且跑得飞快好吧)。
* PHP：你造了一匹特洛伊木马，它每天生产数百匹小马来惩罚你。
*/
```
好吧，我们讨厌手工去维护这么一堆标签！程序员永不为奴！！！(*买烟去~~~*)

## 达夫设备  
> 这个操作实在是太优秀了，据说**第一次看到就能接受**下面这段代码的人，如果不是对编译器非常了解，那么就是对编程一窍不通：  
```c
// 最早达夫设备是用来在内存中拷贝数据的，利用switch 的跌落特性，减少循环中while 判断的次数
// 因为如果循环体的操作比较少的化，判断体对性能的影响就会显得非常重要
// 至于为什么要余8？反正余其他的值也不是不行
// *to = *from++; 的意思就是将from 指向的数据转移到to 指向的位置，然后from 指针后移(自增)
switch(count % 8){
    case 0:
    do {
        *to = *from++;
        case 7: *to = *from++;
        case 6: *to = *from++;
        case 5: *to = *from++;
        case 4: *to = *from++;
        case 3: *to = *from++;
        case 2: *to = *from++;
        case 1: *to = *from++;
        // 注意：没有 break; 哦
    }while((count-=8)>0);
}
```
所以我们也可以用`switch` 替换掉`goto`：

```c  
int function(void){
    static int i, state = 0;
    switch(state){
        case 0:
        for(i=0;i<10;i++){
            state = 1;
            return 1;
            case 1:
            // 继续执行的语句
            ;
        }
    }
}
// 如果用宏定义替换掉这些花里胡哨的结构就更好了
#define crBegin static int state = 0;\
    switch(state){\
        case 0:

#define crReturn(i,x) do{\
    state = i;\
    return x;\
    case i:;\
    }while(0)
// 使用do...while(0)的原因：当crReturn 在if……else…… 中调用时，可以不带花括号
// 在宏定义时很常用的细节
// if(true)
//     do{}while(0);
#define crFinish }

int function(void){
    static int i;
    crBegin;
    for(i=0;i<10;i++)
        crReturn(1,i);
    crFinishi;
}
```  
Perfect，但要注意一些规则：  
    1. 用`crBegin` 和`crFinish` 包围函数体；  
    2. 所有需要保留的变量都声明为`static`；  
    3. 不要将`crReturn` 放在显式的`switch` 语句中；(*显而易见，因为会扰乱达夫设备*)  
    4. 但是这些都还可以接受，毕竟……要啥自行车啊！  
然后还要在`crReturn(i,x)` 中指定参数`i`，难受，但是也有方法解决：ANSI C 提供了一个特殊的宏定义`__LINE__`，表示当前行号  
```c
// 注意要保证宏命令在一行！调用时crReturn 不要在同一行
#define crReturn(x) do{\
    state = __LINE__;\
    return x;\
    case __LINE__:;\
    }while(0);
```

## 评价  
用上面提到的宏命令重写`生产者-消费者`，不要多想，用就行了:
```c
// 解压器
int decompressor(void){
    static int c,len;  // 要保存的环境变量声明在最前
    crBegin;  // 函数开始
    while(1){
        c = getchar();
        if(c == EOF){
            break;
        }
        if(c == 0xFF){
            len = getchar();
            c = getchar();
            while(len--){
                crReturn(c);  // 返回并继续
            }
        }else{
            crReturn(c);  // 返回并继续
        }
    }
    crReturn(EOF);  // 返回并继续
    crFinish;  // 函数结束
}
//解析器
void parser(int c){
    crBegin;  // 函数体开始
    while(1){  // 中间用crReturn 返回值
        if(c == EOF){
            break;
        }
        if(isalpha(c)){
            do{
                add_to_token(c);
                crReturn();
            }while(isalpha(c));
            got_token(WORD);
        }
        add_to_token(c);
        got_token(PUNCT);
        crReturn( );
    }
    crFinish;  // 函数体结束
}
// 如果展开为c 代码，肯定亲妈都不认识👇
void parser(int c){
    static int state = 0;
    switch(state){
        case 0:
        while(1){  // 中间用crReturn 返回值
            if(c == EOF){
                break;
            }
            if(isalpha(c)){
                do{
                    add_to_token(c);
                    do{state = __LINE__;return ;case __LINE__:;}while(0);  // 要保证在一行
                }while(isalpha(c));
                got_token(WORD);
            }
            add_to_token(c);
            got_token(PUNCT);
            do{state = __LINE__;return ;case __LINE__:;}while(0);  // 要保证在一行
        }
    }
}
```
我们把两个方法都重写了，但其实根本没必要。只需要对应的将`crBegin`,`crReturn(x)`,`crFinish` 替换原先函数的代码就好了。*这里的话似乎只实现了`Python` 里面的`generator` 的功能，离协程还有些距离吧*


感觉，如果要实现类似与线程，无阻塞的效果，还需要一个`调度器`来调度定义的`协程`或者说是`generator`，就是：***当一个协程是阻塞状态时，调度器会直接去执行在排队的协程***  

未完待续……