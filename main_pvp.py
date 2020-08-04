from common import BOARD_STAT_BLANK, BOARD_STAT_BLACK, BOARD_STAT_WHITE,\
    PLAYER_HINTS, SPLIT_LINE, input_move, other_side
from board import create_board, clear_board, render_board, render_draw
from path import PATHS, count_paths, check_draw

rounds = 0
board = create_board(BOARD_STAT_BLANK)
side = BOARD_STAT_BLACK


def main_pvp():
    '''Entry point of PvP mode.'''
    global rounds, side
    rounds = 1
    side = BOARD_STAT_BLACK
    clear_board(board)
    loop_pvp()


def loop_pvp():
    '''Game loop of PvP.'''
    global rounds, side

    # info
    print()
    print(SPLIT_LINE)
    print()
    render_board(board)
    print()
    print('Round {} -- {}'.format(rounds, PLAYER_HINTS[side]))
    print()

    # move
    x, y = input_move(board)
    board[y][x] = side

    # check result
    count_results = count_paths(board, side)
    if check_draw(count_results):
        render_draw(board)
        return
    if any(count[0] >= 5 for count in count_results):
        print(SPLIT_LINE)
        print()
        render_board(board)
        print()
        print(
            'Game over. {} wins.'
            .format(PLAYER_HINTS[side])
        )
        return

    # next round
    rounds += 1
    side = other_side(side)
    loop_pvp()
