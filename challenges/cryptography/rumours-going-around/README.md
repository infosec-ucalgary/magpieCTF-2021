
# RumourS going Around
### Category: Cryptography
### Author: Braydon Willms

## Description
Sara said she heard a rumour about me. I also know her friends have been sending her a bunch of messages that I think might be it, but they're encrypted with really big numbers and I don't know what they're saying about me.

We're also given c1.txt, c2.txt, public1.pem, and public2.pem.

## Hint
1. Is bigger really better when you use it too much? 

2. The plaintexts are the same.

## Solution
1. We can start by looking at the public RSA keys we're given. I used pycrypto to read the files.

2. Looking at the keys (and based on the hint), we see that even though the modulus is very large, both keys use the same modulus. We may be able to carry out a common modulus attack.

3. Now we just have to carry out the calculations for this attack. First we run the extended euclidean algorithm with the exponents. Since one of our values is negative (the one corresponding to the first key), we have to find the modular inverse of the first ciphertext. We then compute (c1' ^ -x) (c2 ^ y) (mod n), giving us the message.

(c1'^-x)(c2^y) (mod n)
=(m^(e1\*x+e2\*y)) (mod n)
=m^1

This is also shown in solve.py.

## Flag
magpie{8r0k3N\_h34R73d\_crypt0GR4p3R}
