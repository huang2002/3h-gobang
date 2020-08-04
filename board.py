from common import SIZE, BOARD_STAT_BLANK, BOARD_SYMBOLS,\
    ORD_A, SIDE_HINT, SPLIT_LINE


def create_board(init):
    '''Create an empty board.'''
    return [[init] * SIZE for i in range(SIZE)]


def clear_board(board):
    '''Clear the given board.'''
    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = BOARD_STAT_BLANK


def to_row_str(row):
    '''Convert a row of board stats into a string.'''
    return ' '.join(BOARD_SYMBOLS[x] for x in row)


BOARD_LETTERS = ' ' * 3 \
    + ' '.join(chr(ORD_A + i) for i in range(SIZE))


def render_board(board):
    '''Render the given board.'''
    print(SIDE_HINT)
    print()
    print(BOARD_LETTERS)
    for i in range(SIZE):
        ROW_NUM = str(i + 1)
        print(
            '{:>2}'.format(ROW_NUM)
            + ' '
            + to_row_str(board[i])
            + ' '
            + ROW_NUM
        )
    print(BOARD_LETTERS)


def render_draw(board):
    '''Render the draw ending.'''
    print(SPLIT_LINE)
    print()
    render_board(board)
    print()
    print('Draw.')
