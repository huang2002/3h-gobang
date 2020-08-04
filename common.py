# board size
SIZE = 13

# board stats
BOARD_STAT_BLACK = 1
BOARD_STAT_WHITE = -1
BOARD_STAT_BLANK = 0

# board symbols
BOARD_SYMBOLS = {
    BOARD_STAT_BLACK: '@',
    BOARD_STAT_WHITE: 'O',
    BOARD_STAT_BLANK: '.',
}

# player hints
PLAYER_HINTS = {
    BOARD_STAT_BLACK: 'Black',
    BOARD_STAT_WHITE: 'White',
}

# beginning letter code
ORD_A = ord('A')

# game modes
MODE_PVE = 1
MODE_PVP = 2

# info
SPLIT_LINE = '-' * 30
SIDE_HINT = ' {}: {}; {}: {}'.format(
    BOARD_SYMBOLS[BOARD_STAT_BLACK],
    PLAYER_HINTS[BOARD_STAT_BLACK],
    BOARD_SYMBOLS[BOARD_STAT_WHITE],
    PLAYER_HINTS[BOARD_STAT_WHITE],
)
INPUT_PROMPT = '> '

# AI values
VALUES = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 999,
}
SELF_ADDITION = 1


def other_side(side):
    '''Returns the other side.'''
    return BOARD_STAT_BLACK if side == BOARD_STAT_WHITE else BOARD_STAT_WHITE


def decode_move(move, board):
    '''Parse the given move string into (x, y) coordinate.'''
    assert 2 <= len(move) <= 3

    x = ord(move[0].upper()) - ORD_A
    assert 0 <= x < SIZE

    y = int(move[1:]) - 1
    assert 0 <= y < SIZE

    assert board[y][x] == BOARD_STAT_BLANK

    return (x, y)


def encode_move(x, y):
    '''Encode a move into a-letter-and-a-number form.'''
    return chr(ORD_A + x) + str(y + 1)


def input_move(board, first=True):
    '''Get a validate move.'''
    if first:
        print('Your move: (example: G7; case-insensitive)')
    else:
        print('Please input a valid move:')
    move = input(INPUT_PROMPT)
    print()
    try:
        return decode_move(move, board)
    except AssertionError:
        return input_move(board, first=False)
    except ValueError:
        return input_move(board, first=False)
