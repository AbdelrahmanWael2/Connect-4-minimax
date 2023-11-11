from GUI import show_board, get_user_input

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7


# Function to create an empty Connect 4 board
def create_board():
    board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board


# Main function to run the game
def main():
    # initialization
    board = create_board()
    turn = 0  # 0 for RED (AI) , 1 for YELLOW (player)

    count = 0  # redundant

    # Read user input
    max_depth, with_ab = get_user_input()
    print(max_depth)   # redundant
    print(with_ab)   # redundant

    # Start Game
    while True:
        if turn == 1:
            show_board(board)
            turn = 1 - turn
        else:
            # call minimax to make agent play by only modify board array giving max_depth and with_ab
            print(f"AI {count}")  # redundant
            count = count + 1  # redundant
            turn = 1 - turn


if __name__ == "__main__":
    main()
