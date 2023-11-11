# Function to check if a move is valid
def is_valid_move(board, col):
    return board[0][col] == '0'


# Function to get the next open row in a column
def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == '0':
            return r


# Function to drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece


# Function to check if a player has won the game
def check_winning_move(board, piece):
    return False