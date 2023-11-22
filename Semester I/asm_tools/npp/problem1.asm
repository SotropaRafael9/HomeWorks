bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    array resd 101 ;404 bytes
    count resd 1
    d_format db "%d", 0
    x_format db "%x", 10, 0
    result resw 101 ;202 bytes  
    num_bits resb 101
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, array
        mov [count], dword '0'
        .read_loop:
            ;read numbers from keyboard
            push esi
            push d_format
            call [scanf]
            add esp, 2*4
            ;read until we find 0
            cmp [esi], dword 0
            je .done_read
            
            add esi, 4
            inc dword[count]
            ;read until we have more than 100 numbers
            cmp dword[count], 100
            je .done_read
            
        jmp .read_loop
        .done_read:
        
        mov ecx, [count]
        mov esi, array
        mov edi, result
        
        .loop_1:
            ;calculate the currect word
            mov ah, [esi+2]
            mov al, [esi]
            mov [edi], eax
            
            add esi, 4
            add edi, 2
            

            mov ebx, edi
            sub ebx, result
            shl ebx, 1
            add ebx, num_bits
            mov [ebx], byte 0
            push ecx
            mov ecx, 16
            .count_bits:
                shr ax, 1
                adc byte [ebx], 0
            loop .count_bits
            pop ecx
            
        loop .loop_1
        
        mov esi, 0 ; i=0
        mov edi, 0
        mov ecx, [count]
        dec ecx
        cmp ecx, 0
        je .print
        .sort:
            mov edi, esi
            inc edi ; j = i + 1
            push ecx
            .sort_2:
                mov al, [esi + num_bits] ; al = num_bits[i]
                mov ah, [edi + num_bits] ; ah = num_bits[j]
                cmp al, ah
                jae .skip ;we swich them
                    mov [esi + num_bits], ah
                    mov [edi + num_bits], al
                    
                    mov ax, [2 * esi + result]
                    mov bx, [2 * edi + result]
                    
                    mov [2 * esi + result], bx
                    mov [2 * edi + result], ax
                    
                .skip:
                inc esi
            loop .sort_2
            inc esi
            pop ecx
            inc esi
        loop .sort
        .print
        mov ecx, [count]
        mov esi, result
        .loop_print:
            push ecx 
            mov eax, 0
            lodsw
            push eax
            
                    
                   
            
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
