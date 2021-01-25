# Magpie2021 - Choice of Experience
### Category: Reverse Engineering
### Author: Jeremy Stuart (Mr.Wizard) 

## Description
Just when you thought those MIPS over at Stanford had RISC figured out.  Apple’s got nothing on these Acorns!

## Hints

1. Make sure to put the string into magpie{} when you submit it!

## Solution:
We'll trace through the code to see what it does and include pictures of the commented code.  This assumes you have some knowledge of assembly and how stack frames are work.

1. Notice that the strings are loaded into the .data section, this means they can be overwritten and edited.
        ![01](/assets/01.png)

2. Starting at main, the program allocates the stack frame.  the first loop begins.  Below is commented code to explain the instructions.  The registers keep track of the following:
                x1: the memory address where the string is stored
                x2: tracks how many characters have been manipulated
                w3: stores the character currently being manipulated
                x4: counts the number of times the string has been iterated over
        ![02](/assets/02.png)

3. The second loop XORs each two consecutive letters of str2 together and stores the resulting character over str3.
        ![03](/assets/03.png)

4. The final loop replaces every 2nd character in str3 with the characters of str1
        ![04](/assts/04.png)

5. str3 is printed with the message for the flag.  The stack frame is deallocated, and the program ends.
        ![05](/assets/05.png)


## Flag: 
magpie{th3_|8r1t1sh_4r3_c0m1n6!}
