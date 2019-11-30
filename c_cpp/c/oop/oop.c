#include <stdio.h>

#include "ISay.h"
#include "Human.h"
#include "Coder.h"
#include "Soldier.h"

// test interface
void testInterface(ISay iSay)
{
    iSay.say();
}

int main(void)
{
    // 创建实例
    Coder i = NewCoder(12);
    Soldier s = NewSoldier(21);

    // 测试接口方法
    testInterface(i.iSay);
    testInterface(s.iSay);

    // 模拟里氏转换
    printf("i.age=%d\n", ((pHuman)&i)->age);
    printf("s.age=%d\n", ((pHuman)&s)->age);

    return 0;
}

// 待参考：https://blog.csdn.net/jsc723/article/details/53692570
