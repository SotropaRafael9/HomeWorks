bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf
               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a dd 0
    b dd 0

    message1 db "Introduce the first number : ",13,10,0
    message2 db "Introduce the second number : ", 13, 10, 0
    format db "%d", 0
    ma dd 0
    mesaj_afisare db 'rezultatul este: %x',13,10, 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword message1
        call [printf]
        add esp, 4 * 1
        
        push dword a
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        push dword message2
        call [printf]
        add esp, 4 * 1
        
        push dword b
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        mov cx, 2
        mov eax, dword[b]
        add [a], eax
        mov ax, word[a]
        mov dx, word[a+2]
        div cx        
        mov word[ma], ax

        
        push dword[ma]
        push dword mesaj_afisare
        call [printf]
        add esp, 2*4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
