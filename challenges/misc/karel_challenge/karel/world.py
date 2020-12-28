"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

world.py defines a class that encapsulates the state of Karel the Robot's
world. Methods to load a world from a save file (.w) conforming to the Karel
implementation used in CS106A at Stanford University, and to save the current
state of the world in this format, are also defined.

    Author: Sonny Chan
    Date:   August 2018
"""

import re

from karel import constants
from karel.robot import Karel


class World:
    """
    A World that Karel the robot can live and work in.
    """

    def __init__(self):
        # initialize dimensions of the world
        self.num_avenues = 0
        self.num_streets = 0

        # create empty lists for beepers and walls
        self.beepers = []
        self.walls = []

        # create instance of Karel the Robot
        self.karel = Karel()

        # how fast to run the Karel simulation in this world
        self.speed = 0.5

        # create a default 10x10 world
        self.set_dimensions(10, 10)

    def set_dimensions(self, avenues, streets):
        """
        Reset Karel's world to desired dimensions, clearing everything inside.
        :param avenues: number of avenues (columns)
        :param streets: number of streets (rows)
        :return: None
        """
        # check provided dimensions before continuing
        if avenues < 1 or avenues > constants.MAX_WORLD_AVENUES:
            print("ERROR: Karel's world must have between 1 and 50 avenues")
            exit(-1)
        if streets < 1 or streets > constants.MAX_WORLD_STREETS:
            print("ERROR: Karel's world must have between 1 and 50 streets")
            exit(-1)

        self.num_avenues = avenues
        self.num_streets = streets

        self.beepers = []
        self.walls = []
        for i in range(avenues + 2):                # pad for 1-based index
            avenue_beepers = [0] * (streets + 2)
            avenue_walls = []
            for j in range(streets + 2):
                corner_walls = [False] * 4
                avenue_walls.append(corner_walls)
            self.beepers.append(avenue_beepers)
            self.walls.append(avenue_walls)

        # create walls at the edge of the world
        for i in range(1, avenues+1):
            self.add_wall(i, 1, 'south')
            self.add_wall(i, streets, 'north')
        for j in range(1, streets+1):
            self.add_wall(1, j, 'west')
            self.add_wall(avenues, j, 'east')

    def add_wall(self, avenue, street, direction, remove=False):
        """
        Adds a wall to block off part of the intersection specified.
        Also adds a wall to the adjoining intersection for convenience.
        :param avenue: row coordinate of where to put the wall
        :param street: column coordinate of where to put the wall
        :param direction: one of 'north', 'east', 'south', or 'west'
        :param remove: if set to True, remove instead of add the wall
        :return: None
        """
        if direction == 'north':
            self.walls[avenue][street][constants.NORTH] = not remove
            self.walls[avenue][street + 1][constants.SOUTH] = not remove
        elif direction == 'east':
            self.walls[avenue][street][constants.EAST] = not remove
            self.walls[avenue + 1][street][constants.WEST] = not remove
        elif direction == 'south':
            self.walls[avenue][street][constants.SOUTH] = not remove
            self.walls[avenue][street - 1][constants.NORTH] = not remove
        elif direction == 'west':
            self.walls[avenue][street][constants.WEST] = not remove
            self.walls[avenue - 1][street][constants.EAST] = not remove

    def add_beepers(self, avenue, street, number):
        """
        Adds the specified number of beepers to the given corner.
        :param avenue: row coordinate of where to add the beepers
        :param street: column coordinate of where to add the beepers
        :param number: number of beepers to add
        :return: None
        """
        self.beepers[avenue][street] += number

    def load_from_file(self, filename):
        """
        Read a Karel world description that has been saved to file.
        :param filename: Karel world description (.w)
        :return: True if successful
        """
        beepers = 0
        file = open(filename)
        while True:
            line = file.readline()
            if not line:
                break

            delimit = re.compile(r'[\s:(,)]+')
            tokens = delimit.split(line)
            item = tokens[0]

            if item == 'Dimension':
                avenues = int(tokens[1])
                streets = int(tokens[2])
                self.set_dimensions(avenues, streets)
            elif item == 'Wall':
                avenue = int(tokens[1])
                street = int(tokens[2])
                direction = tokens[3].lower()
                self.add_wall(avenue, street, direction)
            elif item == 'Beeper':
                avenue = int(tokens[1])
                street = int(tokens[2])
                number = int(tokens[3])
                self.add_beepers(avenue, street, number)
            elif item == 'Karel':
                avenue = int(tokens[1])
                street = int(tokens[2])
                direction = tokens[3].lower()
                self.karel = Karel(avenue, street, direction)
            elif item == 'BeeperBag':
                if tokens[1].startswith('INF'):
                    beepers = float('inf')
                else:
                    beepers = float(tokens[1])
            elif item == 'Speed':
                self.speed = float(tokens[1])
        file.close()

        self.karel.beepers = beepers
        return True

    def __str__(self):
        """
        Construct a string that describes this Karel the Robot world in a form
        compatible with the Stanford Karel simulator.
        :return: world description string
        """
        s = 'Dimension: ({}, {})\n'.format(self.num_avenues, self.num_streets)

        # iterate over avenues and streets to output walls and beepers
        for i in range(1, self.num_avenues + 1):
            for j in range(1, self.num_streets + 1):
                walls = self.walls[i][j]
                if walls[constants.WEST] and i > 1:
                    s += 'Wall: ({}, {}) West\n'.format(i, j)
                if walls[constants.SOUTH] and j > 1:
                    s += 'Wall: ({}, {}) South\n'.format(i, j)
                if self.beepers[i][j] > 0:
                    s += 'Beeper: ({}, {}) {}\n'.format(i, j, self.beepers[i][j])

        # output Karel's state
        if self.karel:
            s += str(self.karel)

        # output simulation speed
        s += 'Speed: {:.2f}\n'.format(self.speed)

        return s
