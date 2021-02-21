# Karel
### Category: Misc
### Author: Alexandra Tenney (alexxxii)

## Description
Karel is a robot made by Richard E. Pattis used to teach programming and the logical problem solving skills needed in order to be a programmer in 
1981. It seems like she's trying to tell us something... but I'm not sure what.

## Hints
1. Karel only has four states...

## Solution
The website appears to be a renderer for LaTeX code. Writing LaTex and clicking "Generate PDF" gives a link to a rendered PDf. The output LOG of the LaTeX renderer will also be displayed. 

1. Download and slow down the video or take screenshots at every frame in order to see Karels movements. You should notice she has 4: move, turn left, pick up beeper, put down beeper (this also can be found online with descriptions about Karel).
2. Trace all of these moves.
3. Run the following decryption scrypt to change the sequence of her moves into quaternary, decimal, then ascii. 
```python
from itertools import permutations
import time

def qua_to_decimal(q):
    total = 0
    for i in range(len(q)):
        total += int(q[i]) * 4**(len(q) - i - 1)

    return total

def parse_flag(decimal):

    flag = ""

    lower_bound = 32
    upper_bound = 127

    temp = ""
    for x in str(decimal):
        temp += x
        flag += chr(int(temp))

    return flag

# turn_left => l
# pick_beeper => p
# put_beeper => b
# move => m

moves = [ "lpbl", "lpml", "lplb", "lbmm", "lppl", "lpll", "lbpp", "lmpb", "mblm", "lbmp", "mbmb", "mbml", "llbb", "mbml", "mbll", "llbb", "mblm", "llbb", "mblp", "lbmp", "mbmb", "mblm", "mblb", "llbb", "mblb", "mbmb", "mblm", "lmmb", "lmpm", "mbmb", "lbmp"]

perm = permutations([0, 1, 2, 3])  

for i in list(perm):
    string1 = ""
    flag = ""
    for move in moves:
        print(move)
        for bit in move:
            print(bit)
            if bit == "m":
                string1 += str(i[0])
            elif bit == "l":
                string1 += str(i[1])
            elif bit == "b":
                string1 += str(i[2])
            elif bit == "p":
                string1 += str(i[3])
        print(string1)
        new_string = str(qua_to_decimal(string1))
        flag += chr(int(new_string))
        print(flag)
        string1 = ""
    if "magpie" in flag:
        print(flag)
        break
```

The complete moves list can be found in the script_solution.py file

## Flag
magpiezK4r31_15_4_6r347_734CH3r
magpie{K4r31_15_4_6r347_734CH3r}

