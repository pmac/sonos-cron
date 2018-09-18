import sys

from soco.discovery import by_name


PLAYBAR_NAME = 'Family Room'
PLAYBAR_OBJ = None


def get_playbar():
    global PLAYBAR_OBJ
    if PLAYBAR_OBJ is None:
        PLAYBAR_OBJ = by_name(PLAYBAR_NAME)

    return PLAYBAR_OBJ


def set_night_mode(state):
    """state is boolean"""
    bar = get_playbar()
    if bar.night_mode != state:
        bar.night_mode = state


def set_volume(volume):
    """volume is an int 0 - 100"""
    bar = get_playbar()
    bar.volume = volume


def main(mode):
    if mode == 'day':
        set_night_mode(False)
    elif mode == 'night':
        set_night_mode(True)
        set_volume(15)

    print '{} set to {} mode'.format(PLAYBAR_NAME, mode)


if __name__ == '__main__':
    mode = sys.argv[1]
    main(mode)
