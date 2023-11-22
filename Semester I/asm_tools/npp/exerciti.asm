bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it

import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll

                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    
    a dd 0
    b dd 0
    mesaj_citere_numar1 db 'introduceti primu numar',13, 10, 0
    mesaj_citere_numar2 db 'introduceti al doilea numar',13, 10, 0,
    format db "%d", 0
    sum dd 0
    mesaj_afisare db 'rezultatul este: %x',13,10, 0
    
    ; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword mesaj_citere_numar1  ;print the message
        call [printf]   ;call printf function
        add esp, 1 * 4 ;clear the stack
        
        push dword a    ;put on stack a
        push dword format ;put on stack format
        call [scanf]  ; call scanf function
        add esp, 2 * 4
        
        push dword mesaj_citere_numar2
        call [printf]
        add esp, 1 * 4
        
        push dword b
        push dword format
        call [scanf]
        add esp, 2 * 4
        
        mov eax, [a]
        add eax, [b]
        mov [sum], eax

        
        push dword [sum]  ; put sum on stack
        push dword mesaj_afisare  ;put on stack the message
        call [printf] ; print sum in base 16 and message
        add esp, 2 * 4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
