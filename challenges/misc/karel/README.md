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
        if lower_bound <= int(temp) <= upper_bound:
            flag += chr(int(temp))
            temp = ""

    return flag

moves = [
    ...
]

perm = permutations([0, 1, 2, 3])  
  
# Print the obtained permutations  
for i in list(perm):  
    string1 = ""
    for move in moves:
        if move == "move()":
            string1 += str(i[0])
        elif move == "turn_left()":
            string1 += str(i[1])
        elif move == "put_beeper()":
            string1 += str(i[2])
        elif move == "pick_beeper()":
            string1 += str(i[3])
            

    decodedString = parse_flag(qua_to_decimal(string1))
    if "magpie" in decodedString:
        print(decodedString)
   

```

The complete moves list can be found in the script_solution.py file

## Flag
magpie{K4r31_15_4_6r347_734CH3r}
