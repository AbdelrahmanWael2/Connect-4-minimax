import pygame
import sys
from GameLogic import *

# This is a primitive non-functional GUI that will be modified or more likely built from scratch

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)


# Function to draw the Connect 4 board
def draw_board(board):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(WINDOW, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 0:
                pygame.draw.circle(WINDOW, WHITE,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 1:
                pygame.draw.circle(WINDOW, YELLOW,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(WINDOW, RED,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)


def write_caption():
    pygame.display.set_caption("Connect 4 Game")


# Function to show board to user and waits action
def window_interact(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(WINDOW, 0, (0, 0, COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
            posx = event.pos[0]
            pygame.draw.circle(WINDOW, RED, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get player's move
            posx = event.pos[0]
            col = posx // SQUARE_SIZE

            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                draw_board(board)
                pygame.display.update()
                return False

    draw_board(board)
    pygame.display.update()
    return True

