from common import SIZE, other_side

VECTORS = (
    (-5, 5),
    (0, 5),
    (5, 0),
    (5, 5),
)


def create_paths():
    '''Create paths.'''
    paths = []

    for x0 in range(SIZE):
        for y0 in range(SIZE):
            for dx, dy in VECTORS:
                x1 = x0 + dx
                y1 = y0 + dy
                if -1 <= x1 <= SIZE and y1 <= SIZE:
                    paths.append((x0, y0, x1, y1))

    return tuple(paths)


PATHS = create_paths()  # tuple of (x0, y0, x1, y1)


def walk_path(path):
    '''Get an iterator that walks through the given path.'''
    x0, y0, x1, y1 = path
    dx = (x1 - x0) // 5
    dy = (y1 - y0) // 5
    while x0 != x1 or y0 != y1:
        yield (x0, y0)
        x0 += dx
        y0 += dy


def count_path(path, board, side):
    '''Count the chesses of both sides in the given path of the given board.'''
    chesses = tuple(board[y][x] for x, y in walk_path(path))
    return chesses.count(side), chesses.count(other_side(side))


def count_paths(board, side):
    '''Count all paths of specific side in the given board.'''
    return tuple(count_path(path, board, side) for path in PATHS)


def check_draw(count_results):
    '''Check whether the game is draw.'''
    return all(a * b > 0 for a, b in count_results)
