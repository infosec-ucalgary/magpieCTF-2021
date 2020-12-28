"""
This Karel the Robot program instructs Karel double the number of beepers that
are sitting in a pile in front of him. It illustrates the use of iteration,
testing conditionals, and defining new instructions. It is also a good example
of stepwise refinement and the technique of top-down decomposition.
Run this program with the world described in ex-pile.w.

This example is adapted from the "Karel the Robot Learns Java" handout (2005)
written by Eric Roberts for CS106A at Stanford University.

    Author: Sonny Chan
    Date:   August 2018
"""

from karel import *


def turn_around():
    turn_left()
    turn_left()


def double_into_storehouse():
    """
    Take the pile of beepers at the street corner Karel is standing and place
    twice that many beepers on the corner in front of Karel.
        pre-condition:  Karel is standing on a pile of beepers and the corner
                        in front of him is open.
        post-condition: Karel is standing at the location, facing the same
                        direction, and the corner in front of him has twice
                        the beepers that were previously at his location.
    """
    while beepers_present():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def transfer_beepers_back():
    """
    Take all the beepers at Karel's present location and transfer them to the
    street corner in front of him.
        pre-condition:  The corner in front of Karel is open.
        post-condition: Karel is at the same location and facing the same
                        direction, but all beepers he was standing on have
                        been moved to the corner in front of him.
    """
    while beepers_present():
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_around()


def double_beepers():
    """
    Double the number of beepers on the street corner that Karel is standing.
        pre-condition:  Karel has at least as many beepers in his bag as there
                        are on the corner he's standing, and the street corner
                        in front of him is empty and unblocked.
        post-condition: The corner Karel is standing on has twice as many
                        beepers as were there before.
    """
    double_into_storehouse()
    move()
    turn_around()
    transfer_beepers_back()
    move()
    turn_around()


begin_karel_program()

# assuming there is a pile of beepers at the street corner in front of Karel,
# move forward, double the number of beepers in the pile, and move off the pile
move()
double_beepers()
move()

end_karel_program()
