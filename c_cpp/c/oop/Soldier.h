#include <stdio.h>
#include "Human.h"
#include "ISay.h"
#pragma once
#ifndef __SOLDIER_H__
#define __SOLDIER_H__
// 实例方法
void soldierSay()
{
    printf("soldier say: fire in the hole!\n");
}

// 码农类
typedef struct classSoldier
{
    Human base;
    ISay iSay;
} Soldier, *pSoldier;

// 构造函数
Soldier NewSoldier(int age)
{
    Soldier soldier = {
        age,
        soldierSay};
    return soldier;
}

#endif // 定义Soldier 类