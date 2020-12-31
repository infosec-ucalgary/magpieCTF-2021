#!/usr/bin/env python3

import os
import random


def main():
    dump = "./bin/"
    file_count = 50 # this will take up (file_count / 10) GB of storage

    try:
        os.mkdir(dump)
        print(f"Created {dump}, which will house all {file_count} bin files");
    except FileExistsError:
        print(f"Found pre-existing {dump}, clearing...")

        binfiles = [f for f in os.listdir(dump) if f.endswith(".bin")]
        for f in binfiles:
            os.remove(f"{dump}{f}")

    for i in range(1, file_count):
        binname = f"{hex(random.randint(i* 10000000000, i * 10000000000))[2::]}.bin"
        rand_dump = b"\x00" + os.urandom(100000000) + b"\x00"

        with open(dump+binname, 'wb') as bfile: bfile.write(rand_dump)
        print(f"{dump+binname} has been written")
    
    flag_dump = b"\x00" + os.urandom(99999974) + b"magpie{g00gl3_dr1v3_|)1v3}" + b"\x00"
    with open("bin/25a01c500.bin", 'wb') as lastfile: lastfile.write(flag_dump)
    print(f"bin/25a01c500.bin with the flag has been written")

    return

if __name__ == "__main__": main()
