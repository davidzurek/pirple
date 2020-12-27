import numpy as np


def create_board():
    board = np.zeros((6, 7))
    return board


ROW_COUNT = 6
COLUMN_COUNT = 7


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):


board = create_board()
print(board)
game_over = False
player = 1

while not game_over:
    # ask for player 1 input
    if player == 1:
        col = int(input("Player 1 Make your selection (0-6):\n"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

        player = 2

    # ask for player 2 input
    else:
        col = int(input("Player 2 Make your selection (0-6):\n"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        player = 1

    print_board(board)
