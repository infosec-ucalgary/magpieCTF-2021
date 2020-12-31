 
# DynaTAC 8000x Keylogger
### Category: Forensics
### Author: James Lowther (Articuler)

## Description
The DynaTAC 8000X, released in 1983, was the first consumer cellphone ever sold. Somebody recently modified it to support texting and added a keylogger! Can you find out what message was sent? Note: wrap extracted data in magpie{}


## Hints
1. Take a look at 9-key texting on flip phones.

2. Pay attention to when the keys were actually pressed.

## Solution
This challenge provides you with a file including a bunch of keystrokes on a cell phone as well as the time the key was pressed. Keys need to be decoded to the letters that would be selected if pressed on a 9-key flip phone. The time between each sequence of presses is roughly 400ms and the time between each letter is roughtly 1200ms. The BACKSPACE key represents an incorrect sequence and the user deleting a previously entered letter.

1. To solve this challenge, write a script that looks at the keys and the time they were pressed and decodes each sequence
of key presses back to the corresponding letter on a 9-key flip phone.

## Flag
magpie{itstoobadtextingwasnotevenathingbackthen}