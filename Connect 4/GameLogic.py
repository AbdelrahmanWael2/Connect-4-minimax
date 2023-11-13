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
def check_winning_move(board, piece):
    return False