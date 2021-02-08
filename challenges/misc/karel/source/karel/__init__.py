"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

__init.py__ defines the client interface to our Karel the Robot module.
It sets up the environment so that we can write a karel program with

    from karel import *
    begin_karel_program()
    # give instructions to karel
    end_karel_program()

and we'll have exactly the basic set of instructions and conditions that
Pattis described. Note that the instruction names are slightly different
from those that Pattis used. The names follow those used in CS106A at Stanford
University, but use the underscore convention consistent with Python rather
than the CamelCase convention popular with Java.

    Author: Sonny Chan
    Date:   August 2018
"""

from karel.simulation import *

__all__ = [
    'begin_karel_program', 'end_karel_program',
    'move', 'turn_left', 'pick_beeper', 'put_beeper',
    'front_is_clear', 'left_is_clear', 'right_is_clear',
    'beepers_present', 'beepers_in_bag',
    'facing_north', 'facing_east', 'facing_south', 'facing_west',
    'run_editor_at_finish'
]
