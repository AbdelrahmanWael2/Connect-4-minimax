import Minimax
from Minimax import *
from GameLogic import *
from INode import *
import pygame
import sys
import copy
import tkinter as tk

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
    def submit():
        max_depth_value = max_depth_entry.get()
        alpha_beta_value = alpha_beta_var.get()
        show_tree_value = show_tree_var.get()
        root.destroy()

        # Return the values
        return max_depth_value, alpha_beta_value, show_tree_value

    # Create the main window
    root = tk.Tk()
    root.title("User Input")
    frame = tk.Frame(root, background='#339966', padx=100)
    frame.pack()
    # Create and place the label and entry for max depth
    max_depth_label = tk.Label(frame, background='#339966', text="Enter Max Depth:")
    max_depth_label.pack(pady=5)
    max_depth_entry = tk.Entry(frame)
    max_depth_entry.pack(pady=5)

    # Create and place the checkbox for alpha-beta
    alpha_beta_var = tk.BooleanVar()
    alpha_beta_checkbox = tk.Checkbutton(frame, background='#339966', text="Use Alpha-Beta", variable=alpha_beta_var)
    alpha_beta_checkbox.pack(pady=5)

    # Create and place the checkbox for show tree
    show_tree_var = tk.BooleanVar()
    show_tree_checkbox = tk.Checkbutton(frame, background='#339966', text="Show Tree", variable=show_tree_var)
    show_tree_checkbox.pack(pady=5)

    # Create and place the submit button
    values = tk.Variable()
    submit_button = tk.Button(frame, text="Submit", command=lambda: values.set(submit()))
    submit_button.pack(pady=10)

    # Run the main loop
    root.mainloop()
    return values.get()


def agent_move(board, max_depth):
    c_board = copy.deepcopy(board)
    current_state = INode(c_board, 0, None)
    new_col = minimax(current_state, max_depth, True)[1]
    for child in current_state.children:
        print(child.score)
    Minimax.cache.clear()
    new_row = get_next_open_row(board, new_col)
    WINDOW_SIZE = (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE)
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    drop_piece(board, new_row, new_col, '1', WINDOW)
    draw_board(board, WINDOW)
    return current_state, current_state.children


def show_board(board):
    # Initialize pygame
    pygame.init()
    WINDOW_SIZE = (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE)
    WINDOW = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Connect 4 Game")
    while window_interact(board, WINDOW):
        pass


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
                drop_piece(board, row, col, '2', WINDOW)
                draw_board(board, WINDOW)
                pygame.display.update()
                return False

    draw_board(board, WINDOW)
    pygame.display.update()
    return True
