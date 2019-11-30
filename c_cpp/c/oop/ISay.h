#pragma once
#ifndef __ISAY_H__
#define __ISAY_H__

// interface
typedef struct InterfaceSay
{
    void (*say)();
} ISay, *pISay;

#endif // 定义接口