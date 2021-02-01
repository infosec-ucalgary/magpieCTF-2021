# Mires of Dyrne
### Category: Cryptography
### Author: Emily Baird (analytical engine)

## Description
My friends and I have been playing this cool game called Dungeons and Dragons. It’s really fun! Or, it was really fun, until we got stuck. We found an abandoned temple in a peat bog and started exploring, and now our party is totally lost. The only clue we have is some writing that we found on the wall, but it’s just nonsense. I’m really starting to get frustrated so... I stole a page from our Dungeon Master’s notebook. I hope he doesn’t find out! 

## Hints
1. My character’s name is Blaise. I thought it was boring to be a fighter or a wizard or something, so I made him an alchemist.

2. It feels like we’ve been stuck in this quagmire forever...

## Solution
The cipher is a keyed Vigenere cipher (also called a Quagmire cipher). This cipher is a combination of a substitution cipher that scrambles the Vigenere tableau, followed by a standard Vigenere shift cypher using a keyword. To decrypt the message, 2 keys are needed:
-	The alphabet substitution used to scramble the tableau
-	The Vigenere keyword used to perform the shift

The alphabet substitution can be found on the DM’s notes: 'gfxloqavkntdbczuehwisjpyrm'
The Vigenere keyword can be found by googling the answer to the riddle: ‘candle’

With the two keys, any online decryptor for keyed Vigenere ciphers can be used. In creating this challenge, [this site](http://rumkin.com/tools/cipher/vigenere-keyed.php) was used.

## Flag
magpie{sirvigenereofgreyhawk}
