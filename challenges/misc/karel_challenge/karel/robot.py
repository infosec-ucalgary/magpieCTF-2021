"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

robot.py is a simple class that encapsulates Karel the Robot's internal state.
It includes his location, direction he's facing, and the number of beepers
currently in his bag.

    Author: Sonny Chan
    Date:   August 2018
"""

from karel import constants


class Karel:
    """
    A class to encapsulate Karel the Robot's internal state.
    """

    def __init__(self, avenue=1, street=1, direction='east'):
        # Karel's present location
        self.location_avenue = avenue
        self.location_street = street

        # determine which direction Karel is facing
        if direction == 'north':
            self.facing = constants.NORTH
        elif direction == 'east':
            self.facing = constants.EAST
        elif direction == 'south':
            self.facing = constants.SOUTH
        elif direction == 'west':
            self.facing = constants.WEST
        else:
            self.facing = constants.EAST

        # initialize Karel's beeper bag
        self.beepers = float('inf')

        # set initial error state
        self.error = False
        self.error_message = 'A-OK'

    def __str__(self):
        s = ''
        if self.beepers == float('inf'):
            s += 'BeeperBag: INFINITE\n'
        elif self.beepers > 0.0:
            s += 'BeeperBag: {}\n'.format(int(self.beepers))
        direction = constants.DIRECTION_NAMES[self.facing].capitalize()
        s += 'Karel: ({}, {}) {}\n'.format(self.location_avenue,
                                           self.location_street,
                                           direction)
        return s
