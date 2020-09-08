"""

Create script for DynaTAC 8000x Keylogger challenge
Created for magpieCTF 2021

James Lowther | 2020

"""

from random import randint, choice

# In ms
tap_time = 350
tap_variance = 75
hold_time = 1200
hold_variance = 75

t9_dict = {
    "a" : "2",
    "b" : "22",
    "c" : "222",
    "d" : "3",
    "e" : "33",
    "f" : "333",
    "g" : "4",
    "h" : "44",
    "i" : "444",
    "j" : "5",
    "k" : "55",
    "l" : "555",
    "m" : "6",
    "n" : "66",
    "o" : "666",
    "p" : "7",
    "q" : "77",
    "r" : "777",
    "s" : "7777",
    "t" : "8",
    "u" : "88",
    "v" : "888",
    "w" : "9",
    "x" : "99",
    "y" : "999",
    "z" : "9999"
}

def main():

    # '@' is to represent a backspace 
    flag = "itston@obadtd@extingwaq@q@snotevd@enathh@ingbackthem@n"
    output = open("keylog.txt", "w")

    to_write = "DynaTAC 8000X Keylogger\n" 
    to_write += "-----------------------\n\n"
    to_write += "time (ms) : key\n\n"

    output.write(to_write)

    total_time = 0

    for char in flag:

        # backspace
        if char == '@':
            line = str(total_time) + " : " + "BACKSPACE" + "\n"
            output.write(line)

        else:
            sequence = t9_dict[char]

            for number in sequence:
                total_time += tap_time + randint(0, tap_variance) * choice([-1, 1])
                line = str(total_time) + " : " + str(number) + "\n"
                output.write(line)

        total_time += hold_time + randint(0, hold_variance) * choice([-1, 1])

    line = str(total_time) + " : " + "SEND"
    output.write(line)

    output.close()

main()