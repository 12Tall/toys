#include <stdio.h>
#include "Human.h"
#include "ISay.h"
#pragma once
#ifndef __CODER_H__
#define __CODER_H__
// 实例方法
void coderSay()
{
    printf("coder say: hello world!\n");
}

// 码农类
typedef struct classCoder
{
    Human base;
    ISay iSay;
} Coder, *pCoder;

// 构造函数
Coder NewCoder(int age)
{
    Coder coder = {
        age,
        coderSay};
    return coder;
}

#endif // 定义Coder 类