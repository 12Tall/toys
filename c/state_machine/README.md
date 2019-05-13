# C 语言状态机学习  

参考：[CSND](https://blog.csdn.net/wuhenyouyuyouyu/article/details/52585835) 原文转自[博客园](http://www.cnblogs.com/tangerious/p/4565833.html) 但已不可用  

## 简单的实现  

很容易想到，利用`switch(){case :...;default:break;}` 可以实现，但是程序中判断语句太多的话会导致难以维护，反正个人是不太喜欢太多`if(){...}else{...}` 的。  
文章中提到了[函数式编程](http://www.ruanyifeng.com/blog/2012/04/functional_programming.html)(咱也不懂，不过以后一定会懂的吧)，[尾递归](http://www.ruanyifeng.com/blog/2015/04/tail-call.html)(就可以极大地压缩递归的调用栈吧)。使用函数式编程实现`switch` 语句：**利用函数的指针-->查表**  

## 原理  

```c
typedef unsigned char State;
typedef State(* Procedure)(void *);  
// 定义一个返回 uchar 类型的函数的指针Procedure，需要一个任意类型的指针做参数
// void * 万能指针，可以指向任意类型的地址

// 定义每个状态的处理函数
Procedure Steps[] = {step_init,sterp_count,step_done,step_default};
// step_* 代表函数名

// 定义状态的枚举
enum states = {
    s_init,
    s_count,
    s_done,
    s_default
}
// 枚举类型对应{0,1,2,3}，数组的索引就是状态的定义：

void BestStateMachine(void * invar){
    // 这里的void * 是利用结构体传参，节省栈空间
    static State NS = s_init;  // 定义下一个状态，应该是初始状态吧
    // NS 在每次调用函数时都会得到维护，只需在每个Step 返回下一个状态并保存到NS 就可以实现状态的保存和切换
    NS = Steps[NS](invar);  // 这一句才应该是定义下一个状态
    // 这里应该可以参考[达夫设备](../coroutine/README.md#达夫设备)写一下，应该很好玩才对
}
```

## 实现  

一个[计数器](count.c)的实现