import pygame
import sys

# This is a primitive non-functional GUI that will be modified or more likely built from scratch

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (125, 67, 80)

# Initialize pygame
pygame.init()

# Set the dimensions of the window
WINDOW_SIZE = (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

# Function to create an empty Connect 4 board
def create_board():
    board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board

# Function to draw the Connect 4 board
def draw_board(board):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(WINDOW, RED, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 0:
                pygame.draw.circle(WINDOW, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 1:
                pygame.draw.circle(WINDOW, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

# Main function to run the game
def main():
    board = create_board()
    turn = 0  # 0 for yellow (player), 1 for red (AI)

    pygame.display.set_caption("Connect 4 Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(WINDOW, 0, (0, 0, COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
                posx = event.pos[0]
                pygame.draw.circle(WINDOW, BLUE, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get player's move
                posx = event.pos[0]
                col = posx // SQUARE_SIZE

                if is_valid_move(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 0)
                    pygame.draw.circle(WINDOW, BLUE, (posx, SQUARE_SIZE // 2), event.pos[1])

                    if check_winning_move(board, 0):
                        print("Player wins!")
                        pygame.quit()
                        sys.exit()

                    turn += 1
                    turn %= 2

        draw_board(board)
        pygame.display.update()

# Function to check if a move is valid
def is_valid_move(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Function to get the next open row in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Function to drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if a player has won the game
def check_winning_move(board, piece):
    

    return False

if __name__ == "__main__":
    main()