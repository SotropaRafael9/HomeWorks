; The code below will calculate the result of some arithmetic operations in the EAX register, save the value of the registers, then display the result value and restore the value of the registers.
bits 32

global start        

; declare extern functions
extern exit, printf  
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell assembler function is found in library msvcrt.dll
                          
segment data use32 class=data
	; string of bytes
	format  db "%d", 0  ; %d <=> decimal number
	
segment code use32 class=code
	start:
		; will calculate 20 + 123 + 7 in EAX
		mov eax, 20
		add eax, 123
		add eax, 7         ; eax = 150 (base 10) or 0x96 (base 16)
		
		; save the value of the registers because printf function call will modify their values 
		; use instruction PUSHAD which saves on stack the values of several registers: EAX, ECX, EDX and EBX 
		; in this example the value of EAX must be saved, but the instruction can be generally applied
		PUSHAD
	   
		; will call printf(format, eax) => will print value from eax
		; place parameters on stack from right to left
		push dword eax
		push dword format ; ! address of string on stack, not value
		call [printf]      ; call function for printing
		add esp, 4*2       ; free parameters on the stack; 4 = size of dword; 2 = number of parameters
		
		; after function call printf EAX register has a value set by this function (not the value 150 we have computer at the beginning of the program)
		; restore value of registers saved on stack using POPAD
		; this instruction takes values from the stack and restores them in several registers: EAX, ECX, EDX and EBX
		; it is important that before calling instruction POPAD we make sure there are enough values on stack  
		; to be placed in registers (for example make sure that PUSHAD was called before)
		POPAD
		
		; now value from EAX is restored to its previous value just before calling PUSHAD (in this case, value 150)
		
		; exit(0)
		push dword 0      ; we place on stack parameter for exit
		call [exit]       ; call exit to end the program