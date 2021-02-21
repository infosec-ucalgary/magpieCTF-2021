from itertools import permutations
import time

def qua_to_decimal(q):
    total = 0
    for i in range(len(q)):
        total += int(q[i]) * 4**(len(q) - i - 1)

    return total

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
        for bit in move:
            if bit == "m":
                string1 += str(i[0])
            elif bit == "l":
                string1 += str(i[1])
            elif bit == "b":
                string1 += str(i[2])
            elif bit == "p":
                string1 += str(i[3])
        new_string = str(qua_to_decimal(string1))
        flag += chr(int(new_string))
        string1 = ""
    if "magpie" in flag:
        print(flag)
        break
