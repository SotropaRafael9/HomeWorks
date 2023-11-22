bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit
import exit msvcrt.dll

;data
segment data use32 class=data
    
    a dw 100
    b dw 200
    max resw 1

;code
segment code use32 class=code
start:
    ; unsigned
    ; if (a > b) { 
    ;   max = a;
    ; else {
    ;   max = b;
    ; }
    
    mov ax, [a]
    mov bx, [b]
    
    cmp ax, bx ; compare a with b
    ja a_greater ; if a > b then go to a_greater
    
    ; we get here if a <= b
    mov bx, word [b]
    mov word [max], bx
    jmp fin ; skip over the a_greater lines since we do not need to execute that code
        
    ; we get here if a > b
    a_greater:
        mov bx, word [a]
        mov word [max], bx
        
    fin:
    
    push dword 0
    call [exit]