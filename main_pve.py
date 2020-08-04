from common import BOARD_STAT_BLANK, BOARD_STAT_BLACK, BOARD_STAT_WHITE,\
    SPLIT_LINE, input_move, encode_move
from board import create_board, clear_board, render_board, render_draw
from path import count_paths, check_draw
from ai import find_move, Draw

# AI plays white here

rounds = 0
board = create_board(BOARD_STAT_BLANK)


def main_pve():
    '''Entry point of PvE mode.'''
    global rounds
    rounds = 1
    clear_board(board)
    loop_pve()


def render_info():
    '''Render round info.'''
    print()
    print(SPLIT_LINE)
    print()
    render_board(board)
    print()
    print('Round {}'.format(rounds))
    print()


def loop_pve():
    '''Game loop of PvE.'''
    global rounds

    # render current board
    render_info()

    # move (player)
    player_x, player_y = input_move(board)
    board[player_y][player_x] = BOARD_STAT_BLACK

    # count
    count_results = count_paths(board, BOARD_STAT_BLACK)
    if check_draw(count_results):
        render_draw(board)
        return
    if any(count[0] >= 5 for count in count_results):
        print(SPLIT_LINE)
        print()
        render_board(board)
        print()
        print('Game over. You win.')
        return

    # update board info
    render_info()

    # move (AI)
    try:
        ai_x, ai_y, won = find_move(board, BOARD_STAT_WHITE)
        board[ai_y][ai_x] = BOARD_STAT_WHITE
        print("AI's move: {}".format(encode_move(ai_x, ai_y)))
        if won:
            print()
            print(SPLIT_LINE)
            print()
            render_board(board)
            print()
            print('Game over. You lose.')
            return
    except Draw:
        render_draw(board)
        return

    # next round
    rounds += 1
    loop_pve()
