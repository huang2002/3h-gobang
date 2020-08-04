#!/usr/bin/python
from common import MODE_PVE, MODE_PVP,  INPUT_PROMPT
from main_pve import main_pve
from main_pvp import main_pvp

if __name__ == "__main__":

    print('Welcome to 3h-gobang!')
    print('Please choose the game mode:')
    print('{}: PvE'.format(MODE_PVE))
    print('{}: PvP'.format(MODE_PVP))

    def input_mode():
        try:
            return int(input(INPUT_PROMPT))
        except ValueError:
            return -1

    MODES = {MODE_PVE, MODE_PVP}

    mode = input_mode()
    while not mode in MODES:
        print('Please type a correct game mode number and press Enter.')
        mode = input_mode()

    entry_points = {
        MODE_PVE: main_pve,
        MODE_PVP: main_pvp,
    }
    main = entry_points[mode]
    main()
