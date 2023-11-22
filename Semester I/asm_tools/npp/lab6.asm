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
    s dd 12345607h, 1A2B3C15h
    l equ $-s
    d RESB l
    
    ; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, s
        mov edi, d
        mov ecx, l
        
        jecxz end
        loop_1:
            mov EBX, ESI        ; save the adress of the current byte of s in EBX
            LODSB               ; AL = current byte of s[i]
            push ecx            ; save the counter for loop_1
            push ESI            ; save the adress of the next address
            loop_2:             ; Check the remaining bytes of s and swap them 
                INC esi
                mov AH, [ESI]
                cmp AL, AH
                jg continue
                mov [EBX], AH
                mov [ESI], AL
                mov AL, AH
                continue:
            loop loop_2
            pop ESI
            pop ECX
                
        loop loop_1
        end:  
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
