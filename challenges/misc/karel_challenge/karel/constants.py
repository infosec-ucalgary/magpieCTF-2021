"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

constants.py defines a number of constant data elements that our karel module
uses. Support functions are also defined to obtain paths to the graphical
sprites used to draw the state of Karel and his world.

    Author: Sonny Chan
    Date:   August 2018
"""

import os

# defined directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# direction names
DIRECTION_NAMES = ['north', 'east', 'south', 'west']

# image files
BEEPER_IMAGE_32 = 'beeper.png'
BEEPER_IMAGE_24 = 'beeper24.png'
BEEPER_IMAGE_16 = 'beeper16.png'
KAREL_IMAGE_32 = 'karel.png'
KAREL_IMAGE_24 = 'karel24.png'
KAREL_IMAGE_16 = 'karel16.png'
ERROR_IMAGE = 'error.png'

# max number of streets and avenues in the world
MAX_WORLD_AVENUES = 50
MAX_WORLD_STREETS = 50

# max world size in pixels, for drawing
MAX_WIDTH_PIXELS = 1600
MAX_HEIGHT_PIXELS = 900


def _images_path():
    path = os.path.join(os.path.dirname(__file__), 'images')
    return os.path.abspath(path)


def beeper_image_file(size=32):
    if size < 24:
        return os.path.join(_images_path(), BEEPER_IMAGE_16)
    elif size < 32:
        return os.path.join(_images_path(), BEEPER_IMAGE_24)
    else:
        return os.path.join(_images_path(), BEEPER_IMAGE_32)


def karel_image_file(size=32):
    if size < 24:
        return os.path.join(_images_path(), KAREL_IMAGE_16)
    elif size < 32:
        return os.path.join(_images_path(), KAREL_IMAGE_24)
    else:
        return os.path.join(_images_path(), KAREL_IMAGE_32)


def error_image_file():
    return os.path.join(_images_path(), ERROR_IMAGE)