# Magpie2021 - Paku Paku
### Category: Reverse Engineering
### Author: Jeremy Stuart (Mr.Wizard) 

## Description
Pac is an old friend, he said he'd give you a flag if you could get a new high score!

## Hints

1. Make sure to put the string into magpie{} when you submit it!

## Solution:
This is a Pac-Man ROM for the NES.  It's the original NES release of the game from 1984.  You're told that you'll get a flag if you get a high score, and when you run the game you should immediately notice that the high score is 3,333,360.  Turns out, that's a perfect score in Pac-Man and only three people have ever actually managed to get it, so it's impossible to get a NEW and higher score than that!

NES games are written in 6502 Assembly.  This file has been patched so that when a new high score is achieved then a subroutine runs and writes the flag into the game data/memory (and should be viewable as a string).

There are a few ways to solve this:
1. Change the high score in the NES ROM after the game loads using a debugger or hex editor.  The most common tool for NES hacking is FCEUX.  Using this you can view the memory as hex data, and directly edit the high score.  You need to figure out where the high score is stored in memory, thankfully there are websites to tell you that (I recommend the ROM hacking wiki article at http://datacrystal.romhacking.net/wiki/Pac-Man:RAM_map) Set it to something low so that when you get a high score the flag is written into memory.

2. Patch the subroutine that set the high score to begin with.  I wrote a subroutine in assembly that sets the high score when the game is started.  You can change it to set the high score to something lower.

3. Find the subroutine that writes the flag into memory.  The flag should be viewable in the hex data, but it's seperated by three bytes per character, so it won't be viewable with strings and it might not immediately jump out at you...but if you can find it, it's in there!


## Flag: 
MAGPIE{0RIG1N4L_GH05TBST3R}
