# Opensuse 跨平台编译C  

```bash
# 适用于64 位目标
zypper install mingw64-cross-gcc
zypper install mingw64-cross-gcc-c++

# 编译
x86_64-w64-mingw32-gcc matlab.c -o matlab.exe

# 适用于32 位目标（暂无官方版本）
zypper install mingw32-cross-gcc
zypper install mingw32-cross-gcc-c++
```