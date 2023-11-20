import GUI
import pygame


# Function to check if a move is valid
def is_valid_move(board, col):
    return board[0][col] == '0'


# Function to get the next open row in a column
def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == '0':
            return r


# Function to drop a piece into the board
def drop_piece(board, row, col, piece, window):
    # Starting position at the top of the column
    start_pos_y = 150

    # Ending position at the desired row
    end_pos_y = row * GUI.SQUARE_SIZE + GUI.SQUARE_SIZE // 2 + 100

    # Animation loop
    for current_pos_y in range(start_pos_y, end_pos_y, 8):  # Adjust the step size (5) for speed
        # Redraw board with the piece at its current position
        GUI.draw_board(board, window)
        pygame.draw.circle(window, get_color(piece),
                           (col * GUI.SQUARE_SIZE + GUI.SQUARE_SIZE // 2, current_pos_y),
                           GUI.SQUARE_SIZE // 2 - 5)
        pygame.display.update()
        pygame.time.wait(10)  # Delay for the animation effect (adjust as needed)

    # After the animation, place the piece at the correct position in the board array
    board[row][col] = piece


def get_color(piece):
    if piece == '1':
        return GUI.YELLOW
    elif piece == '2':
        return GUI.RED
    else:
        return GUI.WHITE


# Function to check if a player has won the game
def check_end(board):
    for i in range(len(board[0])):
        if board[0][i] == '0':
            return False
    return True


def calcSoreByRow(board, player):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0]) - 3):
            if (board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player
                    and board[i][j + 3] == player):
                score += 1
    return score


def calcSoreByCol(board, player):
    score = 0
    for j in range(len(board[0])):
        for i in range(len(board) - 3):
            if (board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player
                    and board[i + 3][j] == player):
                score += 1
    return score


def calcSoreByDiagonal(board, player):
    score = 0
    # col index for first 4
    for i in range(len(board[0]) - 3):
        row = 0
        col = i
        while row < len(board) - 3 and col < len(board[0]) - 3:
            if (board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player
                    and board[row + 3][col + 3] == player):
                score += 1
            row += 1
            col += 1

    # row index starting from index = 1
    for i in range(1, len(board) - 3):
        row = i
        col = 0
        while row < len(board) - 3 and col < len(board[0]) - 3:
            if (board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player
                    and board[row + 3][col + 3] == player):
                score += 1
            row += 1
            col += 1

    # last 4 col indices in row 0 in reverse order
    for i in range(len(board[0]) - 1, 2, -1):
        row = 0
        col = i
        while row < len(board) - 3 and col >= 3:
            if (board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player
                    and board[row + 3][col - 3] == player):
                score += 1
            row += 1
            col -= 1

    for i in range(1, len(board) - 3):
        row = i
        col = len(board[0]) - 1
        while row < len(board) - 3 and col >= 3:
            if (board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player
                    and board[row + 3][col - 3] == player):
                score += 1
            row += 1
            col -= 1

    return score


def calcScore(board):
    score1 = calcSoreByRow(board, '1') + calcSoreByCol(board, '1') + calcSoreByDiagonal(board, '1')
    score2 = calcSoreByRow(board, '2') + calcSoreByCol(board, '2') + calcSoreByDiagonal(board, '2')
    return score1, score2
