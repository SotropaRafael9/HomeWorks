bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf,fopen, fclose, fread, fscanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fscanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fclose msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fread msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format_s db "%s", 0
    format_s2 db "%s",10, 0
    format_d db "%d", 0
    format_d2 db "%d",10, 0
    descriptor db 0
    mod_acces db "r",0
    file db "test.txt",0
    text db "dsakdjawuhdwajdpa dwadka idawkmdaw"
    text2 resb 100
    L dd 0
    message_L db "L = ",0
    message_file db "file name  = ",0
    message_text db "Write text", 0
    number resd 1
    fl dd 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...

        
        push dword message_L
        call [printf]
        add esp, 1*4
        
        
        push dword L
        push dword format_d
        call [scanf]
        add esp, 2*4

        
        push dword [L]
        push dword format_d2
        
        call [printf]
        add esp, 2*4
        
        push dword message_file
        call [printf]
        add esp, 1*4
        
        push dword file
        push dword format_s
        call [scanf]
        add esp, 2*4
        
        push dword file
        push dword format_s2
        call [printf]
        add esp, 2*4
        
        push dword mod_acces
        push dword file
        call [fopen]
        add esp, 2*4
        
        mov [fl], eax
        loop_L:
            push dword text2
            push dword format_s
            push dword [fl]
            call [fscanf]
            add esp, 4*3
            
            cmp eax, 0
            jle skip
            
            push dword text2
            push dword format_s
            call [printf]
            add esp, 8 
jmp loop_L            
        ;    jl final_L
        ;    cmp [L], byte 10
        ;    ja final_L
        ;read_text:
        ;    push dword text
        ;    push dword format_s
        ;    push dword [descriptor]
        ;    call [scanf]  
        ;    add esp, 3*4
        ;    
        push dword [L]
        call [printf]
        add esp, 1*4
        
  
        
        skip:
       
        push dword [descriptor]
        call [fclose]
        add esp, 1*4
        final_L:
        final:
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
