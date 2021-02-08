"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

editor.py defines a class that supports basic interactive editing capabilities
for a Karel world. This is very much a work in progress, and only primitive
functionality is available now, but it does get the job done.

    Author: Sonny Chan
    Date:   August 2018
"""

import stddraw

from karel import constants

TOP = 4
BOTTOM = 5


class Editor:
    """
    A class to provide basic editing capabilities for a Karel the Robot world.
    """

    def __init__(self, world, filename='NewKarelWorld.w'):
        """
        :param world: The karel.world instance this editor is associated with
        """
        self._world = world
        self._filename = filename
        self._wall_proximity = 0.1
        self._centre_proximity = 0.25

    def check_events(self):
        if stddraw.mousePressed():
            x = stddraw.mouseX()
            y = stddraw.mouseY()
            localized = self._localize_click(x, y)
            if localized:
                avenue = localized[0]
                street = localized[1]
                location = localized[2]
                if constants.NORTH <= location <= constants.WEST:
                    self._toggle_wall(avenue, street, location)
                elif location == TOP:
                    self._toggle_beeper(avenue, street, 1)
                elif location == BOTTOM:
                    self._toggle_beeper(avenue, street, -1)

        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'p':
                print(self._world)
            elif key == 's':
                with open(self._filename, 'w') as file:
                    file.write(str(self._world))
                print('Saved Karel world to file:', self._filename)

    def _localize_click(self, x, y):
        avenue = int(x) + 1
        street = int(y) + 1

        if not (1 <= avenue <= self._world.num_avenues and
                1 <= street <= self._world.num_streets):
            return ()

        # calculate click point relative to centre of cell
        xc = x + 0.5 - avenue
        yc = y + 0.5 - street
        location = -1

        # check for click near walls
        c = self._centre_proximity
        d = 0.5 - self._wall_proximity
        if xc > d and abs(yc) < d:
            location = constants.EAST
        elif xc < -d and abs(yc) < d:
            location = constants.WEST
        elif yc > d and abs(xc) < d:
            location = constants.NORTH
        elif yc < -d and abs(xc) < d:
            location = constants.SOUTH
        elif abs(xc) < c and abs(yc) < c:
            if yc > 0.0:
                location = TOP
            else:
                location = BOTTOM

        return avenue, street, location

    def _toggle_wall(self, avenue, street, direction):
        # don't toggle the edge walls
        if avenue == 1 and direction == constants.WEST:
            return
        if avenue == self._world.num_avenues and direction == constants.EAST:
            return
        if street == 1 and direction == constants.SOUTH:
            return
        if street == self._world.num_streets and direction == constants.NORTH:
            return

        walls = self._world.walls[avenue][street]
        remove = walls[direction]
        compass = constants.DIRECTION_NAMES[direction]
        self._world.add_wall(avenue, street, compass, remove)

    def _toggle_beeper(self, avenue, street, number):
        beepers = self._world.beepers[avenue][street]
        if beepers + number < 0:
            number = 1
        self._world.add_beepers(avenue, street, number)
