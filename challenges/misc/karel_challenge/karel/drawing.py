"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

drawing.py contains the functions that will draw the state of Karel's world to
the screen. It makes use of the stddraw module within the Booksite Library.

    Author: Sonny Chan
    Date:   August 2018
"""

import pygame

import stddraw
from picture import Picture

from karel import constants

# Picture objects containing the sprites for karel and a beeper
_karel_pictures = []
_beeper_picture = None
_error_picture = None

# Parameters to control visual appearance of world elements
_intersection_size = 0.1
_wall_thickness = 0.04

# Calculated cell (sprite) size to fit the world on the screen
_cell_size = 32

# Estimated proportional font sizes
_font_size_small = 8
_font_size_large = 10


def _calculate_cell_size(avenues, streets):
    """
    Calculates an appropriate Karel world cell size based on the number of
    avenues and streets in the present world.
    :param avenues: number of avenues in Karel's world
    :param streets: number of streets in Karel's world
    :return: cell size, in pixels (power of two)
    """
    cell_width = constants.MAX_WIDTH_PIXELS / float(avenues + 2)
    cell_height = constants.MAX_HEIGHT_PIXELS / float(streets + 1)
    smallest = min(cell_width, cell_height)

    # find highest power of two less than smallest
    cell_size = 16
    while cell_size * 2 < smallest:
        cell_size *= 2

    # special case to allow 24-pixel cell size
    if cell_size == 16 and 24 < smallest:
        cell_size = 24

    return cell_size


def initialize(karel_world):
    """

    :param karel_world: World object that this module can draw
    :return: None
    """
    global _cell_size
    global _font_size_small
    global _font_size_large

    # determine a reasonable canvas cell and canvas size
    na = karel_world.num_avenues
    ns = karel_world.num_streets
    _cell_size = _calculate_cell_size(na, ns)
    cell_dimensions = (_cell_size, _cell_size)

    width = _cell_size * (na + 2) + _cell_size // 2
    height = _cell_size * ns + (3 * _cell_size) // 4
    stddraw.setCanvasSize(int(width), int(height))

    stddraw.setXscale(-0.5, float(na) + 2.0)
    stddraw.setYscale(-0.5, float(ns) + 0.25)

    # choose a reasonable font size
    _font_size_small = max(_cell_size // 4, 8)
    _font_size_large = max(_cell_size // 3, 11)

    # print('cell size is', _cell_size)
    # print('font size is', _font_size_small)

    # create and scale a Picture object for a beeper
    global _beeper_picture
    _beeper_picture = Picture(constants.beeper_image_file(_cell_size))
    surface = _beeper_picture._surface
    _beeper_picture._surface = pygame.transform.scale(surface, cell_dimensions)

    # create and scale a Picture object for Karel's error state
    global _error_picture
    _error_picture = Picture(constants.error_image_file())
    surface = _error_picture._surface
    _error_picture._surface = pygame.transform.scale(surface, cell_dimensions)

    # create, scale, and rotate Picture objects for each of Karel's directions
    for angle in [90, 0, 270, 180]:
        pic = Picture(constants.karel_image_file(_cell_size))
        pic._surface = pygame.transform.scale(pic._surface, cell_dimensions)
        pic._surface = pygame.transform.rotate(pic._surface, angle)
        _karel_pictures.append(pic)


def _draw_labels(avenues, streets):
    stddraw.setFontSize(_font_size_small)
    for i in range(avenues):
        stddraw.text(float(i) + 0.5, -0.2, str(i+1))
    for j in range(streets):
        stddraw.text(-0.2, float(j) + 0.5, str(j+1))


def _draw_status(avenues, streets, karel):
    x = float(avenues) + 1.0
    y = float(streets) - 0.2

    scale = 1.0
    if _cell_size < 32:
        scale = 2.0

    stddraw.setFontSize(_font_size_small)
    stddraw.text(x, y, 'Location:')
    location = '(' + str(karel.location_avenue) + ', ' \
               + str(karel.location_street) + ')'
    stddraw.setFontSize(_font_size_large)
    stddraw.text(x, y - 0.3 * scale, location)

    y -= 0.8 * scale
    stddraw.setFontSize(_font_size_small)
    stddraw.text(x, y, 'Beepers:')
    beepers = '\N{INFINITY}'
    if karel.beepers < float('inf'):
        beepers = str(int(karel.beepers))
    stddraw.setFontSize(_font_size_large)
    stddraw.text(x, y - 0.3 * scale, beepers)

    y -= 0.8 * scale
    stddraw.setFontSize(_font_size_small)
    stddraw.text(x, y, 'Status:')
    if karel.error:
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(x, y - 0.3 * scale, 'ERROR')
    else:
        stddraw.setPenColor(stddraw.DARK_GREEN)
        stddraw.text(x, y - 0.3 * scale, karel.error_message)

    stddraw.setPenColor()
    stddraw.setFontSize(_font_size_small)


def draw_world(world, wait=-1):
    """
    Draws the present state of Karel's world to stddraw.
    :param world: object of type World to draw
    :return:
    """
    stddraw.clear()

    _draw_labels(world.num_avenues, world.num_streets)
    _draw_status(world.num_avenues, world.num_streets, world.karel)

    for i in range(1, world.num_avenues + 1):
        for j in range(1, world.num_streets + 1):
            x = float(i) - 0.5
            y = float(j) - 0.5

            # draw beeper(s) if present
            stddraw.setPenRadius()
            b = world.beepers[i][j]
            if b > 0:
                stddraw.picture(_beeper_picture, x, y)
                if b > 1:
                    stddraw.text(x, y, str(b))
            else:
                d = 0.5 * _intersection_size
                stddraw.line(x - d, y, x + d, y)
                stddraw.line(x, y - d, x, y + d)

            # draw walls
            x1 = x + 0.5
            x0 = x1 - 1.0
            y1 = y + 0.5
            y0 = y1 - 1.0
            walls = world.walls[i][j]
            stddraw.setPenRadius(0.5 * _wall_thickness)
            if walls[constants.NORTH]:
                stddraw.line(x0, y1, x1, y1)
            if walls[constants.SOUTH]:
                stddraw.line(x0, y0, x1, y0)
            if walls[constants.EAST]:
                stddraw.line(x1, y0, x1, y1)
            if walls[constants.WEST]:
                stddraw.line(x0, y0, x0, y1)

    # draw Karel the Robot
    if world.karel is not None:
        x = float(world.karel.location_avenue) - 0.5
        y = float(world.karel.location_street) - 0.5
        d = world.karel.facing
        stddraw.picture(_karel_pictures[d], x, y)
        if world.karel.error:
            stddraw.picture(_error_picture, x, y)

    if wait >= 0:
        stddraw.show(wait)
    else:
        stddraw.show()
