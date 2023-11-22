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
    a db 3
    b db 1
    c db 4
    d db 5 
    ;(5-2*(3-1)+1*4)/2
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AL, [a]
        SUB AL, [b]
        mov BL, 2
        MUL BL
        mov CX, AX 
        mov AL, [b]
        mov DL, [d]
        MUL DL
        mov BX, AX
        mov AX, [d]
        SUB AX, CX
        mov BX, 2
        DIV BL
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
