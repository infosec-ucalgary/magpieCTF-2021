"""
This simple Karel the Robot example contains instructions that cause Karel to
move forward one block, pick up a beeper, then move ahead to the next corner.
It is meant to be run on ex-simple.w, but you can run it on other worlds to
test the Karel simulator's behaviour with things like error conditions.

This example is adapted from the "Karel the Robot Learns Java" handout (2005)
written by Eric Roberts for CS106A at Stanford University.

    Author: Sonny Chan
    Date:   August 2018
"""

from karel import *


begin_karel_program()

move()
pick_beeper()
move()

end_karel_program()
