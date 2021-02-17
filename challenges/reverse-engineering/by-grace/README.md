# Magpie2021 - By Grace
### Category: Reverse Engineering
### Author: Jeremy Stuart (Mr.Wizard) 

## Description
I told Grandma I wanted to be a computer programmer, and she told me that Magpie Machines is always hiring.  She was in the US Navy, but also programmed and helped write their hiring challenge!

## Hints

1. magpiemachines.com

## Solution
There are a few steps and things to solve to get this challengem but there are lots of clues about the theme of the challenge.  The title is "By Grace", the program is COBOL, the varialbe names in the program are all people related to either COBOL or Grace Hopper.  This is an important clue for some of the steps!

1. Navigate on over to magpiemachines.com and just soak it all in.  Spinning gifs, bad backgrounds, it's pure 90s.  Forgive the anachronism, it's supposed to be 80s themed but there weren't really anything that we today would recognize as websites in the 80s.  Notice there's a a careers page.  Go there and find the hiring challenge.  It explains that you need to download a file, decode the data, and get the program.  Once you've done that you have to fix some code and run it.  Then you need to solve the next puzzle and submit the answer as a punch card further down on the page.  Download the file.

2. It's a large tar file!  Untar it to find it's full of pictures of punch cards that all seem to be randomly numbered.  This is acutally a program written on punch cards that we need to decode.  This step is difficult.  Scour the web and find some software to read punch cards.  There's a few out there, but a lot of them aren't maintained and are tempermental.  I don't know of one that quickly and easily reads these cards without some tinkering.  I (Jeremy) built a reader as part of this challenge which if how the "Submit Answer" part works, but you're going to have to figure out how to either manually read the cards or build a program to do it.  I recommend looking up the Python image library.  The best resource I found (and what I used to build mine) was this site: https://iclces.uk/articles/reading_a_punched_card.html.  Once you manage to read a card, read all of them.

3. You get a lot of odd code.  Notice that each line ends with a number.  This is marking which line of code it is in the program.  The lines are all jumbled.  Organize the program into it's proper configuration.

4. What is this weird program?!  A few searches and you should figure out that this is COBOL.  There are a few lines that have <FIX ME> or <ANSWER> in them, but none of them are very specific to the program, and the compiler will likely give you hints about what it needs.  They're part of the lines that every COOBL program should have (except line 37).  You need to figure out what goes there:

        Line 1) `IDENTIFICATION DIVISION.` This is the standard opening line of any COBOL program.

        Line 27) `PROCEDURE DIVISION.` The line that identifies the code section of the program.

        Line 37) This line is calling a subroutine.  The clue on the previous line says "By Grace, is it easier to ask for FORGIVENESS or PERMISSION?".  You should see these two words at the bottom of the code because they're two subroutines, one called FORGIVENESS (sic) and PERMISSION.  If you Google search the clue, the first hit should be a quote from Grace Hopper: "It's easier to ask forgiveness than it is to get permission"  Replace this line with `FORGIVENESS`

        Line 59) Notice that everytime one of these `STRING` blocks starts, it ends with `END-STRING.`

        Line 72) The last line of any COBOL program is `STOP RUN.`

It's important to note here that the mispelling of `FORGIVENESS` is intentional!  Part of the COBOL standard requires that certain "colunms" of the code corresponde to certain types of code.  The tabs in COBOL are important.  Columns 1-4 (characters 1-4) correspond to a certain type of data, and anything in those spaces will be interpreted different if they're written there.  The reason that the word foregiveness is misspelled is because the extra "E" would cause the line to be 73 characters and COBOL only interprets up to 72 characters as code.  I tried to get around this, but was really focused on getting the rest of the challenge working so opted to keep the spelling mistake for convenience!  

5. Now figure out how to run the program.  There are a few options here.  The easiest is probably to use an online COBOL compiler, but be careful!  The FORGIVENESS subroutine does 19061209 loops (doesn't that number look like a date?  Wonder who had a birthday on that day?) and some online compilers will assume the program is stuck in a loop because it takes so long to run.  One that seems to work is https://www.jdoodle.com/execute-cobol-online/.  Another option is to install GNU-COBOL which is a compiler that will compile the program to C, and then to a binary.  I used this when testing the challenge!  The last option is to trace the code by hand.  See the resources section for how to learn some COBOL.

6. Run the program and get this `0x427920477261636520776861742069732031312E3820696E636865733F`.  Looks like hex.  Convert from hex to ASCII to find the line `By Grace what is 11.8 inches?`  Just searching 11.8 inches in Google will only get you a bunch of conversion telling you that it's 29.972 centimeters.  The question is referencing Grace Hopper again though.  You can look at the program and notice all the names are of the variables are people that worked on the COBOL programming language, or Oystein Ore who was Grace Hopper's doctoral supervisor.  It's all about Grace Hopper.  

7. Searching "Grace 11.8 inches" and you'll start to find search results with Grace Hopper explaining that 11.8 inches is the distance light travels in a nanosecond.  Grace Hopper was famous for handing out pieces of wire that were 11.8 inches long to remind programmers what the cost of a nanosecond was.  The answer to the question is a nanosecond.

8. We need to submit the answer on a punch card.  If you looked around the Magpie Machines website, you should have noticed a punch card section that will punch a card for you.  Punch a card with either `nanosecond` or `one nanosecond` or `1 nanosecond` and you should be redirected to a page that congratulates you and gives you the flag as well as some ASCII art of Rear Admiral Dr. Grace Hopper.

## Flag
magpie{4mAz|nG_Gr4c3_h0w_5w33T_Th3_c0d3!!!}

## Resources
If you're looking for help learning COBOL, I'd recommend https://samsclass.info/129S/COBOL.shtml.  This was a CTF based entirely on COBOL and the videos and tutorials on it are fantastic!  It was all developed by Sam Bowne at City College San Francisco, whose entire website is chalk full of excellent infosec resources!

## Special Thanks
A very special thanks to David Bonham of Cambridge, U.K. for his wonderful site https://iclces.uk/articles/reading_a_punched_card.html.  It was a great help in building this challenge!