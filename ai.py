from common import VALUES, SELF_ADDITION, SIZE, BOARD_STAT_BLANK
from path import count_paths, check_draw, PATHS, walk_path
from board import create_board
from random import choice


class Draw(Exception):
    '''Raised when the game is draw.'''


def find_move(board, side):
    '''
    Find a move.

    Returns: (x, y, won)
    '''
    count_results = count_paths(board, side)

    if check_draw(count_results):
        raise Draw

    value_board = create_board(0)

    # calc value
    for path, (self_count, opponent_count) in zip(PATHS, count_results):

        if self_count * opponent_count > 0:
            continue

        if self_count == 4:
            for x, y in walk_path(path):
                if board[y][x] != side:
                    return (x, y, True)

        self_value = VALUES[self_count]
        opponent_value = VALUES[opponent_count]
        value = self_value + opponent_value

        for x, y in walk_path(path):
            value_board[y][x] += value

    # find most valuable
    max_value = 0
    candidates = []
    for x in range(SIZE):
        for y in range(SIZE):
            if board[y][x] != BOARD_STAT_BLANK:
                continue
            value = value_board[y][x]
            if value > max_value:
                max_value = value
                candidates = [(x, y)]
            elif value == max_value:
                candidates.append((x, y))

    # pick one choice from the candidates
    return choice(candidates) + (False,)
