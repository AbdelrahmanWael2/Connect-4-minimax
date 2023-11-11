from Minimax import *
from GameLogic import *
from INode import *
import pygame
import sys
import copy


# This is a primitive non-functional GUI that will be modified or more likely built from scratch

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


def get_user_input():
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 400, 300
    FONT_SIZE = 24

    # Initialize screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("User Input Form")

    # Fonts
    font = pygame.font.Font(None, FONT_SIZE)

    # Input field
    input_rect = pygame.Rect(160, 30, 100, 30)
    input_color = WHITE
    input_text = ''
    input_active = False

    # Checkbox
    checkbox_rect = pygame.Rect(150, 100, 20, 20)
    checkbox_checked = False

    # Submit button
    button_rect = pygame.Rect(150, 150, 100, 30)
    button_color = WHITE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                elif checkbox_rect.collidepoint(event.pos):
                    checkbox_checked = not checkbox_checked
                elif button_rect.collidepoint(event.pos):
                    pygame.quit()
                    return int(input_text) if input_text.isdigit() else 5, checkbox_checked

            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        # Draw everything
        screen.fill((0, 180, 0))

        # Input field
        pygame.draw.rect(screen, input_color, input_rect)
        input_message = font.render("Enter max depth k: ", True, BLACK)
        input_num = font.render(input_text, True, BLACK)
        screen.blit(input_num, (input_rect.x + 1, input_rect.y + 1 ))
        screen.blit(input_message, (5, input_rect.y))

        # Checkbox
        pygame.draw.rect(screen, WHITE, checkbox_rect)
        alpha_message = font.render("Use alph-beta: ", True, BLACK)
        screen.blit(alpha_message, (5, checkbox_rect.y))
        if checkbox_checked:
            pygame.draw.line(screen, BLACK, (checkbox_rect.x + 5, checkbox_rect.y + 5),
                             (checkbox_rect.x + checkbox_rect.width - 5, checkbox_rect.y + checkbox_rect.height - 5), 2)
            pygame.draw.line(screen, BLACK, (checkbox_rect.x + 5, checkbox_rect.y + checkbox_rect.height - 5),
                             (checkbox_rect.x + checkbox_rect.width - 5, checkbox_rect.y + 5), 2)

        # Submit button
        pygame.draw.rect(screen, button_color, button_rect)
        button_surface = font.render("Submit", True, BLACK)
        screen.blit(button_surface, (button_rect.x + 20, button_rect.y + 5))

        pygame.display.flip()


def show_board(board):
    # Initialize pygame
    pygame.init()
    WINDOW_SIZE = (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE)
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Connect 4 Game")
    # c_board = copy.deepcopy(board)
    # test_state = INode(c_board, 0, None)
    # new_col = minimax(test_state, 4, True)[1]
    # new_row = get_next_open_row(board, new_col)
    # drop_piece(board, new_row, new_col, '1')
    # draw_board(board, WINDOW)
    # pygame.display.update()   # remove the comments if you want the ai to play first
    while window_interact(board, WINDOW):
        pass
    c_board = copy.deepcopy(board)
    test_state = INode(c_board, 0, None)
    new_col = minimax(test_state, 4, True)[1]
    new_row = get_next_open_row(board, new_col)
    drop_piece(board, new_row, new_col, '1')
    draw_board(board, WINDOW)
    pygame.display.update()


# Function to draw the Connect 4 board
def draw_board(board, WINDOW):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(WINDOW, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == '0':
                pygame.draw.circle(WINDOW, WHITE,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == '1':
                pygame.draw.circle(WINDOW, YELLOW,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)
            elif board[row][col] == '2':
                pygame.draw.circle(WINDOW, RED,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                                   SQUARE_SIZE // 2 - 5)


# Function to show board to user and waits action
def window_interact(board, WINDOW):

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
                drop_piece(board, row, col, '2')
                draw_board(board, WINDOW)
                pygame.display.update()
                return False

    draw_board(board, WINDOW)
    pygame.display.update()
    return True
