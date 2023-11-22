bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 4
    b dw 16
    c dq 39
    
; our code starts here
segment code use32 class=code
    start:
        ; unsigned
        mov AL, [a]
        MUL byte [a]; AX =  a * a
        mov CX, AX
        mov EAX, 0
        mov AX, CX
        SUB EAX, [b]
        ADD EAX, 7
        mov BL, [a]
        mov BH, 0
        ADD BX, 2
        push EAX
        pop AX
        pop DX
        ;push DX // push AX // pop EAX
        DIV BX
        ;upgrade dw to qw
        mov CX, AX
        mov EAX, 0
        mov AX, CX
        mov EAX, 0
        ADD EAX, [c]
        ADC EDX, [c+4]
        ;signed
        mov AL, [a]
        imul byte [a]
        cwd ;convert
        SUB  AX, [b]
        SBB DX, [b+2]
        ADD AX, 7
        ADC AX 0
        mov BX, AX
        mov Bl, [a]
        mov AL, [a]
        cbw
        ADD AX, 2
        mov CX, AX
        mov AX, BX
        idiv CX
        cwde; EDX:EAX
        ADD EAX, [c]
        ADC EDX, [c+4]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
