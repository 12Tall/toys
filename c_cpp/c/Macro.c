
// 展开宏的宏命令，便于调试
// 2. 将展开后的宏转换成字符串
#define Macro2Str(x) #x
// 1. 此方法将宏展开
#define ParseMacro(x) Macro2Str(x)

#define SIGN(x) INT_##x


#include <stdio.h>
int main(){
    printf("%s\n",ParseMacro(SIGN(2)));
    return 0;
}

