# pe 文件  

## 简介  

`PE`(Portable Execute) 文件是Windows下可执行文件的总称，常见的有DLL，EXE等。  

### 名词  

`虚拟地址`(VA) 每个进程都有自己的4GB 内存，4GB 中的某个位置被称为虚拟地址;  
`基址`(Image_Base) 程序被加载到内存的位置，默认为`0x400000h`(exe)、`0x100000`(dll);  
`相对虚拟地址`(RVA) 为了便于移植，PE 文件中的地址都是按偏移量给的。相对虚拟地址是指：内存中相对载入地址(`基址`)的偏移量，`RVA` = `VA` - `Image_Base`;  
`文件偏移地址`(FOA) 在磁盘中，数据相对于文件头的偏移量;  
`入口点`(OEP) 指向程序入口的相对虚拟地址，一般不只想`main()`  

## 文件结构  

### DOS_HEADER  

```c
struct _IMAGE_DOS_HEADER{
    /* 0x00 */ WORD e_magic;  // magic DOS signature MZ(4Dh 5Ah)|魔术字符串
    /* 0x02 */ WORD e_cblp;  // Bytes on last page of file|最后一页字节数
    /* 0x04 */ WORD e_cp;  // Pages in file|页数
    /* 0x06 */ WORD e_crlc;  // Relocations|重定位元素个数
    /* 0x08 */ WORD e_cparhdr;  // Size of header in paragraphs|头部尺寸，以段落为单位
    /* 0x0a */ WORD e_minalloc;  // Minimun extra paragraphs needs|所需的最小附加段(数?)
    /* 0x0c */ WORD e_maxalloc;  // Maximun extra paragraphs needs|所需的最小附加段(数?)
    /* 0x0e */ WORD e_ss;  // ntial(relative)SS value|初始的SS值（相对偏移量）(RVA?)
    /* 0x10 */ WORD e_sp;  // intial SP value|初始的SP值
    /* 0x12 */ WORD e_csum;  // Checksum|校验和
    /* 0x14 */ WORD e_ip;  // intial IP value|初始的IP值
    /* 0x16 */ WORD e_cs;  // intial(relative)CS value|初始的CS值（相对偏移量）(RVA?)
    /* 0x18 */ WORD e_lfarlc;  // File Address of relocation table|重定位表文件地址
    /* 0x1a */ WORD e_ovno;  // Overlay number|覆盖号
    /* 0x1c */ WORD e_res[4];  // Reserved words|保留字
    /* 0x1e */
    /* 0x20 */
    /* 0x22 */
    /* 0x24 */ WORD e_oemid;  // OEM identifier(for e_oeminfo)|OEM标识符（相对e_oeminfo）
    /* 0x26 */ WORD e_oeminfo;  // OEM information;e_oemid specific|OEM信息
    /* 0x28 */ WORD e_res2[10];  // Reserved words|保留字
    /* 0x2a */
    /* 0x2c */
    /* 0x2e */
    /* 0x30 */
    /* 0x32 */
    /* 0x34 */
    /* 0x36 */
    /* 0x38 */
    /* 0x3a */
    /* 0x3c */ DWORD e_lfanew;  // Offset to start of PE header|PE 头部的文件地址(RVA)
    /* 0x3e */
    /*--------------DOS stub----------------*/
}
```

### PE_HEADER  

这里默认`PE 头` 的地址为00，摘自[看雪学院](https://bbs.pediy.com/thread-247114.htm)  

```c
struct IMAGE_NT_HEADERS{
    /* 0x00 */ DWORD Signature;  // PE signature PE\0\0|魔术字符串
    /* 0x04 */ _IMAGE_FILE_HEADER FileHeader;  // PE 文件头
    /*      */     WORD Machine;  // 运行平台
    /* 0x06 */     WORD NumberOfSections;  // 区块表的个数
    /* 0x08 */     DWORD TimeDataStamp;  // 文件创建时间，是从1970年至今的秒数
    /* 0x0a */
    /* 0x0c */     DWORD PointerToSymbolicTable;  // 指向符号表的指针
    /* 0x0e */
    /* 0x10 */     DWORD NumberOfSymbols;  // 符号表的数目
    /* 0x12 */
    /* 0x14 */     WORD SizeOfOptionalHeader;  // IMAGE_NT_HEADERS结构中OptionHeader成员的大小，对于win32平台这个值通常是0x00e0
    /* 0x16 */     WORD Characteristics;// 文件的属性值

                   /*----- OptionalHeader. 可选文件头 224 bytes -----*/
    /* 0x18 */ IMAGE_OPTIONAL_HEADER32 OptionalHeader;  // 可选文件头
    /*      */     WORD Magic;  // 标志字, ROM 映像（0107h）,普通可执行文件（010Bh）
    /* 0x1a */     BYTE MajorLinkerVersion;  // 链接程序的主版本号
    /* 0x1b */     BYTE MinorLinkerVersion;  // 链接程序的次版本号
    /* 0x1c */     DWORD SizeOfCode;  // 所有含代码的节的总大小
    /* 0x1e */
    /* 0x20 */     DWORD SizeOfInitializedData;  // 所有含已初始化数据的节的总大小
    /* 0x22 */
    /* 0x24 */     DWORD SizeOfUninitializedData;  // 所有含未初始化数据的节的大小
    /* 0x26 */
    /* 0x28 */     DWORD AddressOfEntryPoint;  // 程序执行入口RVA
    /* 0x2a */
    /* 0x2c */     DWORD BaseOfCode;  // 代码的区块的起始RVA
    /* 0x2e */
    /* 0x30 */     DWORD BaseOfData;  // 数据的区块的起始RVA
    /* 0x32 */
                   /*----- NT additional fields. 以下是属于NT结构增加的领域 -----*/
    /* 0x34 */     DWORD ImageBase;  // 程序的首选装载地址
    /* 0x36 */
    /* 0x38 */     DWORD SectionAlignment;  // 内存中的区块的对齐大小
    /* 0x3a */
    /* 0x3c */     DWORD FileAlignment;  // 文件中的区块的对齐大小
    /* 0x3e */
    /* 0x40 */     WORD MajorOperatingSystemVersion;  // 要求操作系统最低版本号的主版本号
    /* 0x42 */     WORD MinorOperatingSystemVersion;  // 要求操作系统最低版本号的副版本号
    /* 0x44 */     WORD MajorImageVersion;  // 可运行于操作系统的主版本号
    /* 0x46 */     WORD MinorImageVersion;  // 可运行于操作系统的次版本号
    /* 0x48 */     WORD MajorSubsystemVersion;  // 要求最低子系统版本的主版本号
    /* 0x4a */     WORD MinorSubsystemVersion;  // 要求最低子系统版本的次版本号
    /* 0x4c */     DWORD Win32VersionValue;  // 莫须有字段，不被病毒利用的话一般为0
    /* 0x4e */
    /* 0x50 */     DWORD SizeOfImage;  // 映像装入内存后的总尺寸
    /* 0x52 */
    /* 0x54 */     DWORD SizeOfHeaders;  // 所有头 + 区块表的尺寸大小
    /* 0x56 */
    /* 0x58 */     DWORD CheckSum;  // 映像的校检和
    /* 0x5a */
    /* 0x5c */     WORD Subsystem;  // 可执行文件期望的子系统
    /* 0x5e */     WORD DllCharacteristics;  // DllMain()函数何时被调用，默认为 0
    /* 0x60 */     DWORD SizeOfStackReserve;  // 初始化时的栈大小
    /* 0x62 */
    /* 0x64 */     DWORD SizeOfStackCommit;  // 初始化时实际提交的栈大小
    /* 0x66 */
    /* 0x68 */     DWORD SizeOfHeapReserve;  // 初始化时保留的堆大小
    /* 0x6a */
    /* 0x6c */     DWORD SizeOfHeapCommit;  // 初始化时实际提交的堆大小
    /* 0x6e */
    /* 0x70 */     DWORD LoaderFlags;  // 与调试有关，默认为 0
    /* 0x72 */
    /* 0x74 */     DWORD NumberOfRvaAndSizes;  // 下边数据目录的项数，这个字段自Windows NT 发布以来一直是16
    /* 0x76 */
    /* 0x78 */     IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];  // 数据目录表 16
    /*      */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0x7a */
    /* 0x7c */         DWORD Size;  // 数据块的长度
    /* 0x7e */
    /* 0x80 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0x82 */
    /* 0x84 */         DWORD Size;  // 数据块的长度
    /* 0x86 */
    /* 0x88 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0x8a */
    /* 0x8c */         DWORD Size;  // 数据块的长度
    /* 0x8e */
    /* 0x90 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0x92 */
    /* 0x94 */         DWORD Size;  // 数据块的长度
    /* 0x96 */
    /* 0x98 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0x9a */
    /* 0x9c */         DWORD Size;  // 数据块的长度
    /* 0x9e */
    /* 0xa0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xa2 */
    /* 0xa4 */         DWORD Size;  // 数据块的长度
    /* 0xa6 */
    /* 0xa8 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xaa */
    /* 0xac */         DWORD Size;  // 数据块的长度
    /* 0xae */
    /* 0xb0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xb2 */
    /* 0xb4 */         DWORD Size;  // 数据块的长度
    /* 0xb6 */
    /* 0xb8 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xba */
    /* 0xbc */         DWORD Size;  // 数据块的长度
    /* 0xbe */
    /* 0xc0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xc2 */
    /* 0xc4 */         DWORD Size;  // 数据块的长度
    /* 0xc6 */
    /* 0xc8 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xca */
    /* 0xcc */         DWORD Size;  // 数据块的长度
    /* 0xce */
    /* 0xd0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xd2 */
    /* 0xd4 */         DWORD Size;  // 数据块的长度
    /* 0xd6 */
    /* 0xd8 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xda */
    /* 0xdc */         DWORD Size;  // 数据块的长度
    /* 0xde */
    /* 0xe0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xe2 */
    /* 0xe4 */         DWORD Size;  // 数据块的长度
    /* 0xe6 */
    /* 0xe8 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xea */
    /* 0xec */         DWORD Size;  // 数据块的长度
    /* 0xee */
    /* 0xf0 */         DWORD VirtualAddress;  // 数据的起始RVA
    /* 0xf2 */
    /* 0xf4 */         DWORD Size;  // 数据块的长度
    /* 0xf6 */
}
```  

**重要**  
`AddressOfEntryPoint`: OEP，程序源入口点  
`ImageBase`: 默认加载基址  
`SectionAlignment`: 内存当中的块对齐数，一般为0x1000  
`FileAlignment`: 磁盘当中块对齐数，一般为0x200  
`SizeOfHeaders`: 所有头部大小 也就是DOS头、文件头以及区块头的总大小，文件主体相对文件其实的偏移  
`IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES]`：数据目录表，保存了各种表的RVA及大小  

### Section_Header  

这里默认`Section 头` 的地址为00，摘自[看雪学院](https://bbs.pediy.com/thread-247303.htm) 

```c
struct _IMAGE_SECTION_HEADER{
    // IMAGE_SIZEOF_SHORT_NAME=8
    /* 0x00 */ BYTE Name[IMAGE_SIZEOF_SHORT_NAME];  // 节表名称,如“.text”
    /* 0x08 */ union {
    /*      */     DWORD PhysicalAddress;  // 物理地址
    /*      */     DWORD VirtualSize;  // 真实长度
    /*      */ } Misc;  // 可以使用其中的任何一个，一般是取后一个
    /* 0x0a */
    /* 0x0c */ DWORD VirtualAddress;  // 节区的 RVA 地址
    /* 0x0e */
    /* 0x10 */ DWORD SizeOfRawData;  // 在文件中对齐后的尺寸
    /* 0x12 */
    /* 0x14 */ DWORD PointerToRawData;  // 在文件中的偏移量
    /* 0x16 */
    /* 0x18 */ DWORD PointerToRelocations;  // 在OBJ文件中使用，重定位的偏移
    /* 0x1a */
    /* 0x1c */ DWORD PointerToLinenumbers;  // 行号表的偏移（供调试使用)
    /* 0x1e */
    /* 0x20 */ WORD NumberOfRelocations;  // 在OBJ文件中使用，重定位项数目
    /* 0x22 */ WORD NumberOfLinenumbers;  // 行号表中行号的数目
    /* 0x24 */ DWORD Characteristics;  // 节属性如可读，可写，可执行等
    /* 0x26 */
}
```

**重要**  
- 以一个空`_IMAGE_SECTION_HEADER` 表示结束  
- 节表的长度比节的实际长度大1  
- 节表的长度在`FileHeader.NumberOfSections` 中指定  

`Name`: 8 位ASCII 码名  
`VirtualAddress`: 区块的RVA  
`SizeOfRawData`: 区块在磁盘文件中的占用大小 200h  
`PointerToRawData`: 文件中的偏移量  
`NumberOfRelocations`：在exe文件中无意义，在OBJ 文件中 是本块在重定位表中重定位数目  

### 文件偏移地址与虚拟地址间的转换  

- 先判断`RVA` 落在哪个区段  
- 减去这个区段的`RVA` 再加上这个区段的`文件偏移量`  
- `文件中的位置` = `虚拟地址` - `区段RVA` + `区段文件地址`

[参考地址1](https://blog.csdn.net/as14569852/article/details/78120335)  
[参考地址2](https://blog.csdn.net/ProgrammeringLearner/article/details/52489794)  

-----  
Maybe if I keep believing my dreams will come to life ...

```txt
  111     222222   TTTTTTTTTTTT            ll  ll  
 1111    22    22   T   TT   T             l l l l  
   11         22        TT                 l l l l  
   11       22          TT       aaaa      l   ll  
   11     22            TT      a    a    ll   l  
   11    22     2       TT      a   aa   l l  ll  l
 111111  22222222       TT       aaa aa    lll lll  
 ```
