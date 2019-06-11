;----------
; Hello World
;----------

.386  ; 386 指令集
.model flat,stdcall  ; (代码和数据使用同一个4GB段) stdcall为API调用时右边的参数先入栈
option casemap:none  ; 大小写敏感

; 引入库
include windows.inc
include user32.inc
includelib user32.lib
include kernel32.inc
includelib kernel32.lib

; data segment
.data
szText db 'Hello World',0  ; 默认ANSI 字符集，汉字乱码

; code segment
.code
start:
    invoke MessageBox,NULL,offset szText,NULL,MB_OK  ; MessgaeBoxA(W) W 代表Unicode 会有乱码的说
    invoke ExitProcess,NULL
end start