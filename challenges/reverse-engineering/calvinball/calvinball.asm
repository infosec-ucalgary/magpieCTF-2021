;*********************************************************************************************
;*
;* CALVINBALL: REVERSE-ENGINEERING SELF-MODIFYING CODE
;*
;* AUTHOR: Emily Baird, Sept 7 2020
;* Many thanks to Karsten Scheibler's introduction to SMC for linux:
;*	http://asm.soureforge.net/articles/smc.html
;*
;* I'm sorry! So sorry! I'm ver
;* 49276d20736f7272792120536f20536f727279212049276d20766572
;* 
;* magpie{m4ke_y0ur_0wn_Ru1ez!}
;* 6d 61 67 70 69 65 7b 6d 34 6b 65 5f 79 30 75 72 5f 30 77 6e 5f 52 75 31 65 7a 21 7d
;*
;*********************************************************************************************

global main								; allow access
extern scanf								; import scanf() for user input


;*********************************************************************************************
;* macro assignment 
;*********************************************************************************************

%assign SYS_WRITE			4
%assign SYS_MPROTECT			125

%assign PROT_READ			1
%assign PROT_WRITE			2
%assign PROT_EXEC			4

;*********************************************************************************************
;* data section 
;*********************************************************************************************
section .data

format:			db "%s", 0					; specify string format for user input
x:			times 28 db 0					; reserve bytes for 28-char input

;*********************************************************************************************
;* calvinball_start
;*********************************************************************************************

section .text

main:

; allow writing into .text section itself
	mov	dword eax, SYS_MPROTECT					; 1st arg: system call opcode (sys_mprotect)
	mov 	dword ebx, main						; 2nd arg: location of section
	and 	dword ebx, 0xfffff000					; 	   page-align location of section
	mov 	dword ecx, 0x1000					; 3rd arg: modify 1 page (4kb)
	mov	dword edx, (PROT_READ | PROT_WRITE | PROT_EXEC) 	; 4th arg: set bits to allow rwx permission
	int	byte 0x80 						; execute syscall
	test 	dword eax, eax						; error handling: check exit code
	js	near calvinball_error					; error handling: jump on error

;*********************************************************************************************
;* main method
;*********************************************************************************************

; print welcome message
print1:
	mov	dword eax, SYS_WRITE					; 1st arg: system call opcode (sys_write)
	mov 	dword ebx, 1						; 2nd arg: file handle (stdout)
	mov	dword ecx, welcome					; 3rd arg: pointer to string
	mov	dword edx, (welcome2 - welcome) 			; 4th arg: length of string
	int	byte 0x80						; execute syscall

; set up XOR garbage	
	mov 	dword [welcome], 0x500a4624				; overwrite welcome with xor flag values
	mov 	dword [welcome+4], 0x1f090a1a				; overwrite welcome with xor flag values

; print welcome message part 2	
	mov 	dword eax, SYS_WRITE					; 1st arg: system call opcode (sys_write)
	mov 	dword ebx, 1						; 2nd arg: file handle (stdout)
	mov	dword ecx, welcome2					; 3rd arg: pointer to string
	mov 	dword edx, (welcome3 - welcome2)			; 4th arg: length of string 
	int 	byte 0x80						; execute syscall

; set up XOR garbage	
	mov 	dword [welcome+8], 0x0c454a4d				; overwrite welcome with xor flag values 
	mov 	dword [welcome+12], 0x1d061016				; overwrite welcome with xor flag values

; take user input using scanf() from C library 
	push	x							; 1st arg: input buf location
	push	format							; 2nd arg: string format
	call	scanf							; execute C library call 
	add	esp, 8							; clean up stack

; set up XOR garbage
	mov 	dword [welcome+16], 0x4f0e422d				; overwrite welcome with xor flag values 
	mov 	dword [welcome+20], 0x5c521b7f				; overwrite welcome with xor flag values 
	mov	dword [welcome+24], 0x0f440c45				; overwrite welcome with xor flag values


; compare bytes from input to flag_fail XOR welcome (welcome is screwed up)
; return value comes back from func in eax: return value is the number of bytes that match between input and flag
comp:
	mov	edi, x							; 1st arg: location of user input
	mov 	esi, flag_fail						; 2nd arg: location of comparison string
	mov 	edx, welcome						; 3rd arg: location of garbled welcome msg
	call 	func							; jump to comparison function
	mov	ebx, eax						; move return value into ebx
	
; set up self-modifying code: NOP instructions are written into EAX, and the return value from func is used 
; to generate an offset to place the NOPs at
	mov  	dword eax, 0x90909090					; move opcode for NOP instruction into eax
	mov	[comp+ebx], eax						; overwrite mem location with NOP
	
; jump to print_fail (GOAL IS TO NOP OUT THIS INSTRUCTION!!)	
	jmp 	print_fail						; unconditional jump over print_success
	
; print success message
print_success:
	mov 	dword eax, SYS_WRITE 					; 1st arg: system call opcode (sys_write)
	mov 	dword ebx, 1						; 2nd arg: file handle (stdout)
	mov 	dword ecx, flag_success					; 3rd arg: pointer to string
	mov 	dword edx, (flag_success2 - flag_success)		; 4th arg: length of string
	int	byte 0x80						; execute syscall

	jmp 	main_end						; skip to end of program
	
	
; print failure message
print_fail:
	mov	dword eax, SYS_WRITE					; 1st arg: system call opcode (sys_write)
	mov	dword ebx, 1						; 2nd arg: file handle (stdout)
	mov 	dword ecx, flag_fail					; 3rd arg: pointer to string
	mov	dword edx, (flag_fail2 - flag_fail)			; 4th arg: length of string
	int	byte 0x80						; execute syscall

; exit with code 0 (no error)
main_end:
	mov	eax, 0
	ret
main_end1:
	nop

;*********************************************************************************************
;* string setup
;*********************************************************************************************

welcome:		db 	"This is my game, so I make the rules.", 10
welcome2:		db 	"Have a flag? Maybe if it's good enough, I'll let you win.", 10
welcome3:

flag_fail:		db 	"I'm sorry! So sorry! I'm very very sorry that I took your precious flag!", 10, "This flag isn't good enough to beat me at Calvinball.", 10
flag_fail2:

flag_success:		db	"Olly-wolly poliwoggy, ump-bump fizz!", 10, "That's my favourite flag, guess you win this one!", 10	
flag_success2:

error_msg:		db 	"encountered error, exited process with code 1", 10
error_msg2:


;*********************************************************************************************
;* comparison function for 2 strings
; 1st arg: location of user input, comes in on edi
; 2nd arg: location of flag_fail string for comparison, comes in on esi
; 3rd arg: location of first XOR second, comes in on edx
;*********************************************************************************************

func:
	push	ebp							; save old base pointer
	mov 	ebp, esp						; set new base pointer to stack pointer
	sub	esp, 4							; make room for 4-byte stack variable
	push	ebx							; store edx

; while loop setup:
	mov	ecx, 0							; initialize loop counter to 0
	mov 	ebx, 3							; initialize correct comparison counter to 0
	jmp 	func_loop_test						; go to loop test

; while loop: 	while(i<28){
; 			if (input byte == (flag XOR welcome)byte)
;				count++
;			advance input byte
;			advance (flag XOR welcome) byte
;		}
func_loop_body:
	inc	ecx							; increment loop counter
	mov 	al, [edi]						; get one byte of user input from memory
	xor	al, [edx]						; xor 1 byte of user input against flag XOR flag_fail
	cmp	al, [esi]						; compare user_input XOR (user_input XOR flag_fail) to flag_fail
	jne	advance							; if they are unequal, do not increment counter
	inc	ebx							; otherwise, increase counter
	
advance:
	inc	edi							; advance to next byte of user input
	inc 	esi							; advance to next byte of  flag_fail
	inc	edx							; advance to next byte of XOR

func_loop_test:
	cmp	ecx, 28							; check value of loop counter 
	jle	func_loop_body						; go to top of loop 

	mov	eax, ebx						; put comparison counter into return var	
	
	pop	ebx
	mov 	esp, ebp						; deallocate stack variables 
	pop 	ebp 							; restore caller's base pointer 
	ret								; return to calling code 

;*********************************************************************************************
;* error handling during setup
;*********************************************************************************************

calvinball_error: 
	mov 	dword eax, SYS_WRITE
	mov	dword ebx, 1
	mov 	dword ecx, error_msg
	mov 	dword edx, (error_msg2 - error_msg)
	int	byte 0x80

	xor	dword eax, eax						; clear eax
	inc	dword eax						; set eax to 1
	mov 	dword ebx, eax						; set ebx to 1
	int	byte 0x80						; syscall (sys_exit, code 1)
