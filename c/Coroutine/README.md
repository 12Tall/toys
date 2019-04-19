# c 语言实现协程  
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