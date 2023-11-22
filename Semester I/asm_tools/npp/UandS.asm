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
        mul bl      ; al = a * b
        mov bx, 25  ; bx = 25
        mul bx      ; al = al * 25
        mov dl, al    
        mov al, [c] ; al = c
        mov dl, 3   ; al = 3
        mul dl      ; al = c * 3
        push eax
        pop ax
        pop dx
        add ax,cx   ;ax=ax + cx
        adc dx,0    
        push ax
        push dx
        pop eax
        mov bl, [a] ;bl = a
        mov cl, [b] ;cl = b
        add bl,cl   ;a+b
        mov bh, 0   ;
        ;adc bh,0
        
        div bx
        
        mov ecx, [x]
        mov edx, [x+4]
        mov bx, ax
        mov eax ,0
        mov ax, bx
        sub ecx, eax
        sbb edx, 0
        add ecx, [e]
        adc edx, 0
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
