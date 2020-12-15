"""

Solve script for cellphone forensics challenge

"""

filename = "keylog.txt"

# In ms
tap_time = 450
hold_time = 1300

t9_dict = {
    "2" : "a",
    "22" : "b",
    "222" : "c",
    "3" : "d",
    "33" : "e",
    "333" : "f",
    "4" : "g",
    "44" : "h",
    "444" : "i",
    "5" : "j",
    "55" : "k",
    "555" : "l",
    "6" : "m",
    "66" : "n",
    "666" : "o",
    "7" : "p",
    "77" : "q",
    "777" : "r",
    "7777" : "s",
    "8" : "t",
    "88" : "u",
    "888" : "v",
    "9" : "w",
    "99" : "x",
    "999" : "y",
    "9999" : "z"
}

def main():

    # Read in the challenge data
    in_file = open(filename, "r")
    data = in_file.readlines()[5:]

    c_time = 0
    seq = ""
    flag = ""

    for line in data:
        x = line.rstrip("\n")
        (time, key) = x.split(" : ")

        # Calculate change in time
        delta_time = int(time) - c_time

        # Intermediate key press
        if delta_time < tap_time:
            seq = seq + key

        # Letter selected
        else:
            if seq:
                flag = flag + t9_dict[seq]

            if key == "BACKSPACE":
                flag = flag[:-1]
                seq = ""

            else:
                seq = key

        c_time = int(time)

    print(flag)

    in_file.close()

main()
