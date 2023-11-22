bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, sum               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format db "%d",0
	a db 1
	b db 2
	c db 4
	e dw 5
	x dq 1000
	;x-(a*b*25+c*3)/(a+b)+e
; our code starts here
segment code use32 class=code
    start:
        ; ...
		mov AL, [a]
		MOV CL, 25
		MUL CL ; 25
		mov BL, [b]
		MUL BL ;BL IS THE RESULT =50
		MOV DL, [c]
		MOV AH, 3 ;
		MUL AH;12
		ADD BL, AH ; 62 ; BL IS THE RESULT
		MOV BH, 0
		
		
		MOV AL, 0
		MOV AL, [a]
		mov CL, 0
		MOV CL, [b]
		add AL, CL
		MOV AH, 0
		MOV CX, [e]
		ADD AX, CX
		
		MOV DX, BX
		DIV DX
		
		
		
		
		
		
		
		
		
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]  