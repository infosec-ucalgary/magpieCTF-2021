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
    "turn_left()",
    "pick_beeper()",
    "move()",
    "put_beeper()",
    "pick_beeper()",
    "turn_left()",
    "turn_left()",
    "pick_beeper()",
    "move()",
    "turn_left()",
    "move()",
    "put_beeper()",
    "pick_beeper()",
    "turn_left()",
    "pick_beeper()",
    "turn_left()",
    "pick_beeper()",
    "put_beeper()",
    "pick_beeper()",
    "pick_beeper()",
    "put_beeper()",
    "move()",
    "turn_left()",
    "pick_beeper()",
    "put_beeper()",
    "put_beeper()",
    "turn_left()",
    "pick_beeper()",
    "pick_beeper()",
    "turn_left()",
    "pick_beeper()",
    "put_beeper()",
    "pick_beeper()",
    "pick_beeper()",
    "turn_left()",
    "put_beeper()",
    "move()",
    "move()",
    "put_beeper()",
    "pick_beeper()",
    "turn_left()",
    "put_beeper()",
    "put_beeper()",
    "put_beeper()",
    "turn_left()",
    "turn_left()",
    "move()",
    "pick_beeper()",
    "turn_left()",
    "pick_beeper()",
    "move()",
    "put_beeper()",
    "pick_beeper()",
    "turn_left()",
    "turn_left()",
    "move()",
    "move()",
    "turn_left()",
    "pick_beeper()",
    "put_beeper()",
    "pick_beeper()",
    "pick_beeper()",
    "put_beeper()",
    "move()",
    "pick_beeper()",
    "turn_left()",
    "turn_left()",
    "turn_left()",
    "put_beeper()",
    "move()",
    "move()",
    "pick_beeper()",
    "move()",
    "turn_left()",
    "pick_beeper()",
    "pick_beeper()",
    "put_beeper()",
    "pick_beeper()",
    "move()",
    "turn_left()",
    "turn_left()",
    "move()",
    "put_beeper()",
    "move()",
    "put_beeper()",
    "turn_left()",
    "pick_beeper()",
    "pick_beeper()",
    "move()",
    "put_beeper()",
    "put_beeper()",
    "put_beeper()",
    "pick_beeper()",
    "move()",
    "pick_beeper()",
    "turn_left()",
    "move()",
    "put_beeper()",
    "put_beeper()",
    "move()",
    "move()",
    "move()",
    "put_beeper()",
    "move()",
    "pick_beeper()",
    "pick_beeper()",
    "pick_beeper()",
    "pick_beeper()",
    "move()",
    "pick_beeper()",
    "move()",
    "put_beeper()",
    "turn_left()",
    "move()",
    "put_beeper()",
    "pick_beeper()",
    "turn_left()",
    "move()",
    "pick_beeper()",
    "move()",
    "put_beeper()",
    "turn_left()"
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
   