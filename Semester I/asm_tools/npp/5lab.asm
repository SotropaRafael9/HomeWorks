bits 32 
global start        


extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    ; ...
    a db 1, 2, 3
    l1 equ $-a ;length of a
    b db 9, 8, 7
    l2 equ $-b ;length of b 
    r times l1 + l2 db 0 ;reserves enough bytes for the destination string

;Two byte strings A and B are given. Obtain the string R by concatenating the elements of B in reverse order and the odd elements of A.
segment code use32 class=code
    start:
        
        mov edi, r  
        mov esi, b + l2 - 1 ;esi ca sa inceapa de la sf sirului
        mov ecx, l2
        jecxz EndLoop
        StartLoop:
            mov al, [esi] ;
            dec esi
            mov [edi], al
            inc edi
            Loop StartLoop
        EndLoop:
        
        mov esi, a
        mov ecx, l1
        StartLoopB:
            mov al, [esi]
            inc esi
            mov dl, 00000001b
            and dl, al
            cmp dl, 1
            je StartIf
            jne EndIf
            StartIf:
                mov [edi], al
                inc edi
            EndIf:
        loop StartLoopB
               
        
        ; exit(0)
        push    dword 0      
        call    [exit]       
