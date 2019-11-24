def chessboard(N: int, board:list=None, queen_positions:set =set()):
    # If no chessboard was passed create a new one
    if board is None:
        board = {(x, y) for x in range(N) for y in range(N)}

    # Remove all unsuitable cells:
    for x_queen, y_queen in queen_positions:
        board = {(x,y) for x, y in board
                 if (x != x_queen) and (y != y_queen) and (abs(y - y_queen) != abs(x - x_queen))}

    if not board:
        return queen_positions

    possible_solutions = []

    for cell in board:
        qp_copy = queen_positions.copy()
        qp_copy.add(cell)

        # iterate over possible solution:
        possible_solutions.append(chessboard(N, board, qp_copy))

    # Remove duplicates:
    solutions = []
    [solutions.append(s) for s in ]
    return possible_solutions


print(chessboard(3))