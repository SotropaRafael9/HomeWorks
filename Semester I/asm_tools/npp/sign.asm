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
    a db 20
    b db 20
    c db 3
    e dd 5
    x dq 300
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;x-(a*b*25+c*3)/(a+b)+e
        mov al, [a] ; al = a
        mov bl, [b] ; bl = b
        imul bl ;
        mov bx, 25
        imul bx
        mov cl, [c]
        mov dl, 3
        mul dl
        push eax
        pop ax
        pop dx
        mov  
        add ax,cx
        
        adc dx,0
        push ax
        push dx
        pop eax
        mov bl, [a]
        mov cl, [b]
        add bl,cl
        mov edx, eax
        mov al, bl
        cbw 
        mov bx, ax
        mov eax, edx
        push eax
        pop ax
        pop dx
        
        idiv bx
        mov ecx, [x]
        mov edx, [x+4]
        sbb cx, ax
        adc ecx, [e]
        adc edx, 0
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
