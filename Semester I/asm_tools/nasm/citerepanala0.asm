bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fprintf, fopen, fclose, gets               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fclose msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fprintf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import gets msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format db "%s",10,13,0
    descriptor dd 0
    modacces db "w",0
    file db "Text2.txt"
    cuv db 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword modacces
        push dword file
        call [fopen]
        mov esp, 2*4
        
        mov [descriptor], eax
        loop_cuv:
            push dword cuv
            call [gets]
            mov esp, 1*4
            
            cmp [cuv], byte '0'
            je final
            
            push dword cuv
            push dword format
            push dword [descriptor]
            call[fprintf]
            mov esp, 3*4
        
        mov esp, 2*4
        
        push dword [descriptor]
        call [fclose]
        add esp, 1*4
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
