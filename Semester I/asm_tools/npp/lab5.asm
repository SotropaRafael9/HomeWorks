bits 32 
global start        


extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    ; ...
    a db "123"
    l1 equ $-a ;length of a
    b db "987"
    l2 equ $-b ;length of b 
    r times l1 + l2 db 0 ;reserves enough bytes for the destination string

; Two character strings A and B are given. Obtain the string R by concatenating the elements of B in reverse order and the elements found on even positions in A.

segment code use32 class=code
    start:
        mov ecx, (l2 + 1) // 2 
        mov esi, 0
        PushAToStack: 
            mov al, [a + esi]
            inc esi
            mov ah, [a + esi]
            inc esi
            push ax
        loop PushAToStack
        
        
        mov ecx, l2
        test ecx, 1
        mov esi, 0
        jpe LengthOfBIsEven 
            pop ax
            mov [r + esi], al 
            inc esi
            dec ecx
            ; muta in rezultat jumatate din cat a fost scos din stiva pentru ca va fi un element random daca length u sirului este impar
        LengthOfBIsEven:
            PopReversedAToR: ;scoate din stiva elementele din stiva si le pune in R 2 cate 2
                pop ax
                mov [r + esi], ah
                inc esi
                mov [r + esi], al
                inc esi
                dec ecx
            loop PopReversedAToR
        mov ecx, 10
        mov esi, a
        jz out 
            
                
            
        
        
       
        
        
        ; exit(0)
        push    dword 0      
        call    [exit]       
