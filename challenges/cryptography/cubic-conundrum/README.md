
# Cubic Conundrum
### Category: Cryptography
### Author: Braydon Willms

## Description
I'm so excited about my brand new rubik's cube that I didn't want to stop at solving it - so now I'm encrypting with it!

We're also given cubic\_conundrum.pdf.

## Solution
1. The first thing we need to do is read through the pdf to see how this challenge works. We're given 5 sequences of moves corresponding to encrypted cubes. We can apply each of these to a solved cube using an online tool (make sure the colors line up).

2. We're also given the sequence of moves used to encrypt the data. If we to decrypt it, we'll just have to reverse that sequence of moves. The decryption key is U2 L' U D' R.

3. After applying the given sequences followed by the decryption key to solved cubes, we can read the colors off and decode them according to the given base 4 scheme to get the flag.

## Flag
magpie{(u63\_m4G!c}
