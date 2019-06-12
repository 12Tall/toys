;----------
;通用程序框架
;----------

.386
.model flat, stdcall
option casemap: none

include windows.inc
include user32.inc
includelib user32.lib
include kernel32.inc
includelib kernel32.lib
include comdlg32.inc
includelib comdlg32.lib

ICO_MAIN equ 1000
DLG_MAIN equ 1000
IDC_INFO equ 1001
IDM_MAIN equ 2000
IDM_OPEN equ 2001
IDM_EXIT equ 2002
IDM_1 equ 4000
IDM_2 equ 4001
IDM_3 equ 4002
IDM_4 equ 4003

.data  ; 数据段
hInstance dd ?  ; dd 进程实例句柄
hRichEdit dd ?  ; dd 富文本动态链接库句柄
hWinMain dd ?  ; 窗口句柄
hWinEdit dd ?  ; 文本控件句柄
szFileName db MAX_PATH dup(?)

.const  ; 常量段?
szDllEdit db 'RichEd20.dll',0
szClassEdit db 'RichEdit20A',0
szFont db '宋体',0

.code  ; 代码段

_init proc  ; 窗口初始化子程序
    ; 局部变量@var:type
    local @stCf:CHARFORMAT

    invoke GetDlgItem, hWinMain, IDC_INFO

    mov hWinEdit, eax

    ; 为窗口设置图标
    invoke LoadIcon, hInstance, ICO_MAIN
    invoke SendMessage, hWinMain, WM_SETICON, ICON_BIG, eax

    ; 设置编辑器控件
    invoke SendMessage, hWinEdit, EM_SETTEXTMODE, TM_PLAINTEXT, 0
    invoke RtlZeroMemory, addr @stCf, sizeof @stCf
    mov @stCf.cbSize, sizeof @stCf
    mov @stCf.yHeight, 9*20
    mov @stCf.dwMask, CFM_FACE or CFM_SIZE or CFM_BOLD
    invoke lstrcpy, addr @stCf.szFaceName, addr szFont
    invoke SendMessage, hWinEdit, EM_SETCHARFORMAT, 0, addr @stCf
    invoke SendMessage, hWinEdit, EM_EXLIMITTEXT, 0, -1
    ret
_init endp

; uses 用于让编译器保护相关寄存器
_ProcDlgMain proc uses ebx edi esi hWnd, wMsg, wParam, lParam
    mov eax, wMsg
    .if eax == WM_CLOSE
        invoke EndDialog, hWnd, NULL
    .elseif eax==WM_INITDIALOG  ; 初始化
        push hWnd
        pop hWinMain
        call _init
    .elseif eax==WM_COMMAND  ; 菜单
        mov eax, wParam
        .if eax == IDM_EXIT  ; 退出
            invoke EndDialog, hWnd, NULL
        .elseif eax == IDM_OPEN  ; 打开文件
        .elseif eax == IDM_1  ; 打开其他菜单项
        .elseif eax == IDM_2  
        .elseif eax == IDM_3  
        .elseif eax == IDM_4  
        .endif
    .else
        mov eax, FALSE
        ret
    .endif
    mov eax, TRUE
    ret
_ProcDlgMain endp

start:
    invoke LoadLibrary, offset szDllEdit
    mov hRichEdit, eax
    invoke GetModuleHandle, NULL
    mov hInstance, eax
    invoke DialogBoxParam, hInstance, DLG_MAIN, NULL, offset _ProcDlgMain, NULL
    invoke FreeLibrary, hRichEdit
    invoke ExitProcess, NULL
    end start