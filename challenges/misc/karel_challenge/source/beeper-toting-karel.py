"""
This Karel the Robot program instructs Karel to pick up a beeper from 1st
street and carry that beeper to the centre of a ledge on 2nd street.
Run this program with the world specified in ex-simple.w.

This example is adapted from the "Karel the Robot Learns Java" handout (2005)
written by Eric Roberts for CS106A at Stanford University.

    Author: Sonny Chan
    Date:   August 2018
"""

from karel import *


begin_karel_program()

# move forward and pick up the beeper
move()
pick_beeper()

# move forward, turn the corner, and go to the centre of the 2nd street ledge
move()
turn_left()
move()
turn_left()
turn_left()
turn_left()
move()
move()

# put the beeper down and move forward again
put_beeper()
move()

end_karel_program()
