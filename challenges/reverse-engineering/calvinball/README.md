# Calvinball
### Category: Reverse Engineering
### Author: Emily Baird (Analytical Engine)

## Description
"The only rule in Calvinball is that you can never play with the same rules twice. Speaking of rewriting the rules, I think there's something fishy going on with this program...

## Hints
Take a look at that syscall at the beginning of main.

## Solution:
The challenge can be solved by tracing the execution of the assembly. 

    1. a sys_mprotect call is made at the beginning of main, and that it is being used to give rwx permissions to the .text section (normally a read-only section). This means that the memory addresses of the instructions themselves can be accessed and overwritten

    2. notice that areas of the .text section are indeed being written over with seemingly random hex values

    3. Before the call to “comp” is made, three arguments are set up: one is the memory location where user input is stored, one is the memory location of one of the print messages, and one is the location of the random bytes that were written in earlier

    4. Inside comp, tracing execution will show that a single byte of input is XORed against the “random” hex values, and then compared to the values of the print message. If the two match, a counter is increased, and this counter is returned in EAX

    5. Upon return from comp, another memory address is again being overwritten. This time, the address points to instructions themselves, and is calculated using the return value from comp - if the return value is high enough (as in, every byte within the comp function matched), the code that is overwritten will be the “jmp print_fail” line, which will be replaced by NOP. The code will then proceed to “print_success”

A good chunk of the trace can be skipped by a player who tries XORing the “random” bytes with the memory location without bothering to follow the full flow.


## Flag: 
magpie{m4ke_y0ur_0wn_Ru1ez!}
