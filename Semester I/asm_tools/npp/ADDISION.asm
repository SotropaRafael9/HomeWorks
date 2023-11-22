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
    a db 1 
    b dw 3  
    c dd 10
    d dq 15
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; a - byte, b - word, c - double word, d - quad word
        
        ; a + b + c + (d - a)
        
        mov EAX, 0
        mov AL, [a]
        ADD AX, [b] ;  AX = a + b
        ADD EAX, [c] ; EAX = AX + c
        
        mov EBX, EAX  ; EBX <= EAX
        mov EAX ,[d]  ; EAX <= primi 4 bytes a lui d
        mov EDX ,[d+4] ; EDX <= ultimi 4 bytes a lui d
        SUB AL, [a]    ; EDX:EAX - a 
        ADD EAX, EBX ; EDX:EAX + EBX
        ADC EDX, 0
            
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
