bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fprintf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fprintf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file db 'text.txt',0
    text db 'a1#$hjhj989012noipudjksanldi8q2#@!#@!!8nmn1luh21n!@#$m#%KADAWDE@!$@!DSR#@AS',13,10, 0
    modacces db 'w',0
    descriptor dd 0
    format db '%s', 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword modacces  ; put modacces to stack
        push dword file  ; put file to stack
        call [fopen] ; opens a file
        add esp, 2 * 4
        cmp eax, 0  
        
        je final
        mov [descriptor], eax ;
        mov ebx, 0
        
        Parcurge:
            cmp [text+ebx], byte 0 ; verfy if the current caracter is null caracter and comp the current caracter if it is in  0-33 ascii code
            je Scrie
            cmp [text+ebx], byte 33
            jae verfy1
            
            jmp Continue
            
        verfy1:
            cmp [text+ebx], byte 47
            jbe special_caracter
            ; very in ascii code 33-47 if is special caracters
            cmp [text+ebx], byte 58
            jae verfy2
            jmp Continue
            
            
        verfy2:
            cmp [text+ebx], byte 64
            jbe special_caracter
            ; 58-64
            jmp Continue
            
        special_caracter:
            mov [text+ebx], byte 'X' ; if is special caracter it replays it with 'X'
        Continue:
            inc ebx
            jmp Parcurge
        
        Scrie:
        push dword text
        push dword format
        push dword [descriptor]
        call [fprintf]
        add esp, 3 * 4
        
        final:
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
