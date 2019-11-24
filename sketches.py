def chessboard(N: int, board:list=None, queen_positions:list=[]):
    # If no chessboard was passed create a new one
    if board is None:
        board = [(x, y) for x in range(N) for y in range(N)]

    # Remove all unsuitable cells:
    for queen_x, queen_y in queen_positions:
        # Remove horizontal ones:
        [board.remove((x, queen_y)) for x in range(N) if (x, queen_y) in board]
        # Remove vertical lines:
        [board.remove((queen_x, y)) for y in range(N) if (queen_x, y) in board]
        # Remove diagonals:
        [board.remove((x, x + abs(queen_x - queen_y)))
         for x in range(-N,N) if (x, x + abs(queen_x - queen_y)) in board]
        [board.remove((y + abs(queen_x - queen_y), y))
         for y in range(-N, N) if (y + abs(queen_x - queen_y), y) in board]

    # If no empty cells left, return []:
    if not board:
        return []

    # Initialize solutions list:
    solutions = []

    # Iterate over empty cells and create different solutions:
    for empty_cell in board:
        # Place queen into the cell:
        queen_positions.append(empty_cell)

        # duplicate current queen positions for further iterations:
        solutions = queen_positions[:]

        # Add solution sequence for each possible placement:
        for placement in chessboard(N, board, queen_positions):
            solutions.append(queen_positions.extend(placement))

    # remove duplicated lists:
    # Sort each solution and path it to queen_positions:
    solutions = [sorted(s) for s in solutions]
    queen_positions = []
    [queen_positions.append(s) for s in solutions if s not in queen_positions]

    return queen_positions

