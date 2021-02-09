# Text-Adventure
### Category: Misc
### Author: Joshua Novak (rm -rf /0797), Emily Baird (Analytical Engine4954) and Brandon Arenas (Inga5508)


# Binary Room

## Hints
No hints. Everything needed is given in print statements.

## Solution
Solution is to overwrite the 9 byte password. The real obstacle is giving gets a null byte right after the first password so that strcmp will not compare the entire 256 byte buffer. Instead, it will stop at the 10th byte, the null byte. 

For a detailed solution, see exploit.py in solve/

## Flag
magpie{d()nt_p@n!k_pIz}
