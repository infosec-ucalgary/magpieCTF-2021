
# Data Encryption (non)Standard
### Category: Cryptography
### Author: Braydon Willms

## Description
There's a lot of talk about DES, but how hard can it be to make a block cipher? I bet you can't break mine!

We're also given server\_no\_flag.py.

## Hints
1. I'm not sure what the big deal is about key schedules, but I think it'll be fine. 

2. Well, I guess I did borrow the structure from DES...

## Solution
1. We start by looking at the block cipher in the program we're given. There are a lot of weaknesses in this cipher, such as a relatively small key size or weak keys (and likely a variety of other attacks). However, the following attack will be sure to run in the time we have during the CTF.

2. The first thing to notice is that the round keys are just switched between the halves of the original key for the cipher. This means the cipher is essentially just an iteration of the same two rounds repeated several times. We also see that we can calculate the key quite easily from the input and output of these two rounds, so we can use a slide attack here.

3. The number of queries we can make is also limited to 2^12. However, since the cipher uses a feistel network (the same structure as DES), we can optimize our slide attack to work with this many plaintext-ciphertext pairs.

4. Now, we can find the key by carrying out a slide attack with a twist. We encrypt and decrypt 2^10 messages, where the halves that remain unchanged after one round are the same. These sets of messages will be out of phase by one round, and we can search by a slid pair by looking for a pair where both the plaintext of one encrypts to the plaintext of the other, and the ciphertext of the first encrypts to the ciphertext of the second (though we're technically decrypting one of the pairs, encryption and decryption follow the same structure here) for some key. This gives us half of the key, and we can reverse the halves that we keep the same and repeat this process to find the other half. As this is a probabilistic attack, we may have to retry a few times.

For more details, take a look at dens\_solve.py, or you can find the attack described here
https://www.iacr.org/archive/eurocrypt2000/1807/18070595-new.pdf

## Flag
magpie{T74t'5\_a\_F31StY\_C19HeR}
