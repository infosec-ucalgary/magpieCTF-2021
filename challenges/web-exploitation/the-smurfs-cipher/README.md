# The Smurfs Cipher
### Category: Web Exploitation
### Author: James Lowther (Articuler)

## Description
Gargamel stole the key to decrypt The Smurfs ciphertext. Now they can't get into their kingdom to view their flag. Can you help them get the right key?

## Solution
This challenge gives you a file named `cipher` and the source code used to return the flag. Your goal is to reverse engineer the source code to create, and upload, the key that will allow the flag to be returned. This challenge requires you to exploit PHP loose comparison. In PHP versions less than 8 using `==` will loosly compare variables of different types, allowing expressions to implicitly evaluate to true. Any string (i.e. `password.txt`) compared with the integer `0` will evaluate to `true`. By making `to_check` equal to `0` we can echo the flag.

A table showing all of the PHP loose comparison values can be found [here](https://www.php.net/manual/en/types.comparisons.php).

1. In order to get the flag we need to ensure that `$to_check` is `0` to exploit PHP using loose comparison.
2. Create a 8 byte file that is equivalent to the the data in `cipher + 0xd34db33f` and upload it.
    * Your key will be XORed with `cipher + 0xd34db33f`. If they are equivalent then the XOR result will be zero.
3. The if statement will be `0 == "whatever the password is"` which evaluates to true, and the flag will be echoed back.

## Flag
magpie{l0053_c0mp4r150n_l34d5_t0_tr0ub13}