# heuristicX is responsible for taking the board from nodes and evaluating the
# score of the current state based on many factors: connected pieces, edge
# avoidance, center control, opponent blocking ...
# aw
def calc_score(board):
    def horizontal_window(start_row, start_column):
        agent_pieces, opp_pieces, empty = 0, 0, 0

        for k in range(start_column, start_column + 4):
            if board[start_row][k] == '1':
                agent_pieces += 1
            elif board[start_row][k] == '2':
                opp_pieces += 1
            else:
                empty += 1

        return compute_score(agent_pieces, opp_pieces, empty)

    def vertical_window(start_row, start_column):
        agent_pieces, opp_pieces, empty = 0, 0, 0

        for k in range(start_row, start_row + 4):
            if board[k][start_column] == '1':
                agent_pieces += 1
            elif board[k][start_column] == '2':
                opp_pieces += 1
            else:
                empty += 1

        return compute_score(agent_pieces, opp_pieces, empty)

    def diagonal_window(start_row, start_column, slope):
        agent_pieces, opp_pieces, empty = 0, 0, 0

        for k in range(start_row, start_row + 4):
            if board[k][start_column] == '1':
                agent_pieces += 1
            elif board[k][start_column] == '2':
                opp_pieces += 1
            else:
                empty += 1

            start_column += 1 if slope == 'p' else -1

        return compute_score(agent_pieces, opp_pieces, empty)

    # checking connected pieces
    def compute_score(agent_pieces, opp_pieces, empty):
        WIN_SCORE = 100
        THREE_PIECES_ONE_EMPTY_SCORE = 20
        TWO_PIECES_TWO_EMPTY_SCORE = 6

        # blocking mechanism
        LOSE_SCORE = -150
        OPPONENT_THREE_PIECES_ONE_EMPTY_SCORE = -60
        OPPONENT_TWO_PIECES_TWO_EMPTY_SCORE = -6

        if agent_pieces == 4:
            return WIN_SCORE
        elif agent_pieces == 3 and empty == 1:
            return THREE_PIECES_ONE_EMPTY_SCORE
        elif agent_pieces == 2 and empty == 2:
            return TWO_PIECES_TWO_EMPTY_SCORE
        elif opp_pieces == 4:
            return LOSE_SCORE
        elif opp_pieces == 3 and empty == 1:
            return OPPONENT_THREE_PIECES_ONE_EMPTY_SCORE
        elif opp_pieces == 2 and empty == 2:
            return OPPONENT_TWO_PIECES_TWO_EMPTY_SCORE
        return 0

    def compute_score_with_middle_bonus():
        position_score = 0
        SCORE_MATRIX = [
            [3, 4, 5, 7, 5, 4, 3],
            [4, 6, 8, 10, 8, 6, 4],
            [5, 8, 11, 13, 11, 8, 5],
            [5, 8, 11, 13, 11, 8, 5],
            [4, 6, 8, 10, 8, 6, 4],
            [3, 4, 5, 7, 5, 4, 3]
        ]

        for m in range(ROWS):
            for n in range(COLUMNS):
                if board[m][n] == '1':
                    position_score += SCORE_MATRIX[m][n]
                elif board[m][n] == '2':
                    position_score -= SCORE_MATRIX[m][n]

        return position_score

    score = 0
    ROWS = 6
    COLUMNS = 7
    # horizontal check
    for i in range(ROWS):
        for j in range(COLUMNS - 3):
            score += horizontal_window(i, j)

    # vertical check
    for j in range(COLUMNS):
        for i in range(ROWS - 3):
            score += vertical_window(i, j)

    # diagonal check
    for i in range(ROWS - 3):
        for j in range(COLUMNS - 3):
            score += diagonal_window(i, j, 'p')
            score += diagonal_window(i, COLUMNS - j - 1, 'n')

    score += compute_score_with_middle_bonus()

    return score
