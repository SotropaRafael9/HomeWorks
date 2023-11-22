bits 32 ; assembling for the 32 bits architecture

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 class=code
    string:
        mov eax, 0x00 ;or 0
        mov edi, 1
        mov ecx, [esp + 4] ;clear 
        loop_1:
            inc ecx
            cmp [ecx], byte '1'
            jne loop_1 ;if is not equal goes back to loop 1
            mov ebx, [esp + 4]
        loop_build_eax:
            dec ecx 
            cmp [ecx], byte '1'
            jne loop_build_eax_end_if
            add eax, edx ;
        loop_build_eax_end_if:
            shl edx, 1
            cmp ecx, ebx
            jne loop_build_eax         
        
        ; exit(0)
        ret
