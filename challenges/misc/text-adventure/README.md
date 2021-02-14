# Text-Adventure
### Category: Misc
### Author: Joshua Novak (rm -rf /0797), Emily Baird (Analytical Engine4954) and Brandon Arenas (Inga5508)

---

# OSINT
## Description
In our text adventure, you find traces of a certain nerdy employee! It seems like he obsessed over a certain song. Look around very carefully and using the power of deduction (and your favourite search engine) figure out the name of that song!

## Hints
1. When submitting the flag, it should be all lowercase and separated by underscores: magpie{fake_answer_to_OSINT_here}
2. As this is an OSINT challenge, be sure to make use of your favourite search engines!

## Solution
1. Find all clues
  - Whip
  - NES in computer room drawer
  - Tape player
  - Notice poster
2. Deduce (this is really up in the air as it could be very different from person to person):
  - Notice
    - It's June
    - Jim playing video game music
    - Jim obsessed with month old game (game came out in May)
  - NES
    - Probably Jim's. Hence, game is a NES game
  - Whip
    - Jims whip (written on it).
    - If this was a video game toy: NES + whip + 80s = Castlevania
  - Stereo
    - Tape labelled epic battle music: Some kind of battle music from Castlevania
    - When you use the stereo it prints music out:
      - Here you have to figure out the sound of the piece of music and get its title
  - Flag
    - Once you know all of the above: the piece of music is "Nothing To Lose", the final boss themes in Castlevania.

## Flag
magpie{nothing_to_lose}

---

# Binary Room
## Description
Dracula left his terminal open. It's password protected but he's not very good at programming. He really should stick to evil magic...

## Hints
No hints. Everything needed is given in print statements.

## Solution
Solution is to overwrite the 9 byte password. The real obstacle is giving gets a null byte right after the first password so that strcmp will not compare the entire 256 byte buffer. Instead, it will stop at the 10th byte, the null byte. 

For a detailed solution, see exploit.py in solve/

## Flag
magpie{d()nt_p@n!k_pIz}
