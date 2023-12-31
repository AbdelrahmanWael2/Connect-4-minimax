from GUI import show_board, get_user_input, agent_move
from DrawTree import *

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7


# Function to create an empty Connect 4 board
def create_board():
    board = [['0' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board


# Main function to run the game
def main():
    # initialization
    board = create_board()
    turn = 1  # 0 for RED (AI) , 1 for YELLOW (player)

    # Read user input
    max_depth, with_ab, treeDraw = get_user_input()
    max_depth = int(max_depth)
    print(max_depth, with_ab, treeDraw)
    # Start Game
    while True:
        if turn == 1:
            show_board(board)
            turn = 1 - turn
        else:
            parent, tree = agent_move(board, max_depth, with_ab)
            if treeDraw == 1:
                drawTree(parent, 0, None, with_ab)
            turn = 1 - turn


if __name__ == "__main__":
    main()
