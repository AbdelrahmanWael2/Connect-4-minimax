import math
import random
import GUI
import INode
import copy
from GUI import *
from GameLogic import *
from heuristicX import *
from INode import *


def get_valid_locations(board):
    valid_locations = []
    for col in range(GUI.COLUMN_COUNT):
        if is_valid_move(board, col):
            valid_locations.append(col)
    return valid_locations


def is_terminal_state(board):
    return len(get_valid_locations(board)) == 0


# The main minimax algorithm
def minimax(state, depth, is_maximizing):
    # Check if the game is over or if the maximum depth is reached
    game_over = is_terminal_state(state.board)
    if depth == 0 or game_over:
        if game_over:
            # If the game is over, return a score of 0 and None (no played column)
            return 0, None
        else:
            # If the maximum depth is reached, return the calculated score and None
            return calc_score(state.board), None

    # Get the valid locations for the next move
    valid_locations = get_valid_locations(state.board)

    # Initialize the played column with a random choice from valid locations
    played_col = random.choice(valid_locations)

    # Maximizing player's turn
    if is_maximizing:
        score = -math.inf
        for col in valid_locations:
            row = get_next_open_row(state.board, col)
            # Make a copy of the board and drop a piece in the current column
            new_board = copy.deepcopy(state.board)
            drop_piece(new_board, row, col, '1')
            # Create a new state and recursively call minimax for the next level
            new_state = INode(new_board, depth - 1, state)
            new_score = minimax(new_state, new_state.depth, False)[0]
            # Update the score and played column if a better move is found
            if new_score > score:
                score = new_score
                played_col = col
        return score, played_col
    # Minimizing player's turn
    else:
        score = math.inf
        for col in valid_locations:
            row = get_next_open_row(state.board, col)
            # Make a copy of the board and drop a piece in the current column
            new_board = copy.deepcopy(state.board)
            drop_piece(new_board, row, col, '2')
            # Create a new state and recursively call minimax for the next level
            new_state = INode(new_board, depth - 1, state)
            new_score = minimax(new_state, new_state.depth, True)[0]
            # Update the score and played column if a better move (with respect to the AI) is found
            if new_score < score:
                score = new_score
                played_col = col
        return score, played_col

