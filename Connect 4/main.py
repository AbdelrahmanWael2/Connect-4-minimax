from GUI import write_caption, window_interact

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100


# Function to create an empty Connect 4 board
def create_board():
    board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board


# Main function to run the game
def main():
    board = create_board()
    turn = 0  # 0 for RED (AI) , 1 for YELLOW (player)
    count = 0
    write_caption()
    while True:
        if turn == 1:
            while window_interact(board):
                pass  # wait user to play
            turn = 1 - turn
        else:
            # call minimax to make agent play by only modify board array
            print(f"AI {count}")  # redundant
            count = count + 1  # redundant
            turn = 1 - turn


if __name__ == "__main__":
    main()
