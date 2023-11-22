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
    a dw 0111011101010111b     
    b dw 0110111001010010b  
    c resd 1
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;Given the words A and B, compute the doubleword C as follows:
        ;the bits 0-2 of C have the value 0
        ;the bits 3-5 of C have the value 1
        ;the bits 6-9 of C are the same as the bits 11-14 of A
        ;the bits 10-15 of C are the same as the bits 1-6 of B
        ;the bits 16-31 of C have the value 1
        mov bx, 0FFFFh ;we compute the result in bx
        ;and bl, 11111000b ;we shift the 1 s in ebx to have first 8 bits 1
        shl ebx, 16 
        or bl, 00111000b ;we put last 3-5 bits numbers to be 1
        mov cx, [a]  ;mov  a to cx
        shr cx, 11   ;shift to the right to have
        shl cx, 6
        or bx, cx  
        mov dx, [b]
        shr dx, 1
        shl dx, 10
        or bx, dx
        
        
       
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
