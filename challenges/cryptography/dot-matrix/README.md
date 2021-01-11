
# Dot Matrix
### Category: Cryptography
### Author: Braydon Willms

## Description
This stupid dot matrix printer makes so much noise, jams, and I can't figure out what it did to my picture! 

Note: Don't try to print a file you value.

We're also given the file flag.png and a binary named printer.

## Hint
I swear I'm going to throw this thing down a hill!

## Solution
In this challenge, we're given a file with a png extension, though it isn't a proper png, and a binary that was run on the file.

1. Start by reverse engineering the binary (I used cutter). We see that the binary starts by running the function gen\_enc\_matrix, which generates an array of 4 random chars. It then reads a file specified by the command line, and runs the function encrypt\_file and overwrites the original file with the result.

2. Based on the matrix generation function, the operations performed by encrypt\_file, and the hint, we can determine that the encyrption uses a hill cipher with a 2x2 matrix. However, we also have to note that the modulus is determined by the size of a byte, and is 256 rather than 26.

3. Based on the file extension, the file was orginially a png. Using the magic number of a png (0x89504e47), we can set up a system of linear congruences and find the encryption matrix.

4. Finally, find the inverse of this encryption matrix, and use it to decrypt the picture, which contains the flag.

solve/dot\_matrix\_solve.py shows how we can carry out this decryption process.

## Flag
magpie{4t\_L3a5T\_T73\_p4P3R\_15\_7uN}
