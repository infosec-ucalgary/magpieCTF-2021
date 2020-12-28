"""
An implementation of Karel the Robot as described by Richard E. Pattis in
Karel the Robot: A Gentle Introduction to the Art of Programming, 2nd ed.
(John Wiley & Sons, 1995). This implementation has Karel using Python 3 syntax
and relies on the Booksite Library supporting Introduction to Programming in
Python by Robert Sedgewick, Kevin Wayne, and Robert Dondero.
https://introcs.cs.princeton.edu/python/home/

simulation.py is the client's primary interface to Karel. It defines the four
basic instructions that Karel can execute as well as the conditions on the
world that he can test. In this implementation, all Karel commands should be
sandwiched by the pair of begin_karel_program() and end_karel_program()
statements.

    Author: Sonny Chan
    Date:   August 2018
"""

import sys

from karel import constants, drawing
from karel.world import World
from karel.editor import Editor

_world = World()
_karel = _world.karel

_wait = 250.0
_allow_edit = False

# location increments for moving north, east, south, and west, respectively
_step_avenue = [0, 1, 0, -1]
_step_street = [1, 0, -1, 0]


def begin_karel_program():
    global _karel
    global _wait

    # if first command line argument is specific, assume it is a world file
    #if len(sys.argv) >= 2:
    _world.load_from_file("worlds/challenge-world.w")
    _karel = _world.karel
    #else:
        #print("WARNING: No world specified, we'll let Karel run in an empty world.")
        #print("         (World file to load can be given as first command argument.)")

    # set simulation speed and wait time
    speed = _world.speed
    if len(sys.argv) > 2:
        speed = float(sys.argv[2])
    if speed >= 1.0:
        _wait = 0.0
    else:
        _wait = 1000.0 / (2.0 ** (4.0 * speed))

    drawing.initialize(_world)
    _update()


def end_karel_program():
    if _allow_edit:
        _run_editor_loop()
    else:
        drawing.draw_world(_world, -1)


def move():
    if not _ready():
        return

    # check for walls
    d = _karel.facing
    walls = _world.walls[_karel.location_avenue][_karel.location_street]
    if walls[d]:
        _error('Crashed into a wall.')
        return

    _karel.location_avenue += _step_avenue[d]
    _karel.location_street += _step_street[d]
    _update()


def turn_left():
    if not _ready():
        return

    # directions are ordered N, E, S, W, so turn left goes backward in the list
    _karel.facing = (_karel.facing - 1) % 4
    _update()


def pick_beeper():
    if not _ready():
        return

    # check that there is a beeper in the world
    a = _karel.location_avenue
    s = _karel.location_street
    if _world.beepers[a][s] < 1:
        _error('No beeper to pick up.')
        return

    _world.beepers[a][s] -= 1
    _karel.beepers += 1.0
    _update()


def put_beeper():
    if not _ready():
        return

    # check that Karel has a beeper in his bag
    if _karel.beepers <= 0.0:
        _error('No beepers in bag to place.')
        return

    a = _karel.location_avenue
    s = _karel.location_street
    _karel.beepers -= 1.0
    _world.beepers[a][s] += 1
    _update()


def front_is_clear():
    if not _ready():
        return False
    d = _karel.facing
    return not _world.walls[_karel.location_avenue][_karel.location_street][d]


def left_is_clear():
    if not _ready():
        return False
    d = (_karel.facing - 1) % 4
    return not _world.walls[_karel.location_avenue][_karel.location_street][d]


def right_is_clear():
    if not _ready():
        return False
    d = (_karel.facing + 1) % 4
    return not _world.walls[_karel.location_avenue][_karel.location_street][d]


def beepers_present():
    if not _ready():
        return False
    a = _karel.location_avenue
    s = _karel.location_street
    return _world.beepers[a][s] > 0


def beepers_in_bag():
    if not _ready():
        return False
    return _karel.beepers > 0.0


def facing_north():
    if not _ready():
        return False
    return _karel.facing == constants.NORTH


def facing_east():
    if not _ready():
        return False
    return _karel.facing == constants.EAST


def facing_south():
    if not _ready():
        return False
    return _karel.facing == constants.SOUTH


def facing_west():
    if not _ready():
        return False
    return _karel.facing == constants.WEST


def run_editor_at_finish():
    global _allow_edit
    _allow_edit = True


def _ready():
    if _karel is None or _karel.error:
        return False
    return True


def _update():
    drawing.draw_world(_world, _wait)


def _error(message):
    _karel.error = True
    _karel.error_message = message
    print('ERROR SHUTOFF:', _karel.error_message)
    end_karel_program()


def _run_editor_loop():
    ed = Editor(_world)
    while True:
        _update()
        ed.check_events()


def _main():
    begin_karel_program()
    move()
    put_beeper()
    put_beeper()
    move()
    turn_left()
    move()
    turn_left()
    end_karel_program()


if __name__ == '__main__':
    _main()
