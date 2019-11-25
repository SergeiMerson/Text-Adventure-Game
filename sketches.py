"""
def check_horizontal(row, queens_on_board):
    return any(row == queen[0] for queen in queens_on_board)


def check_vertical(col, queens_on_board):
    return any(col == queen[1] for queen in queens_on_board)


def check_diagonal(row, col, queens_on_board):
    return any([abs(row - queen[0]) == abs(col - queen[1]) for queen in queens_on_board])


def cell_is_suitable(row, col, queens_on_board):
    return not any([
        check_horizontal(row, queens_on_board),
        check_vertical(col, queens_on_board),
        check_diagonal(row, col, queens_on_board)
    ])
"""

# Get file from disk:
book_path = r"D:\Projects\Experis\Exercises\Project_Guttenberg\The_Black_Arrow.txt"
stopwords_path = r"D:\Projects\Experis\Exercises\Project_Guttenberg\stopwords.txt"

with open(stopwords_path, 'r', encoding='UTF-8') as stopwords_file:
    stopwords = set([symbol.strip() for symbol in stopwords_file.readlines()])



with open(book_path, 'r', encoding='UTF-8') as book_file:
    current_line = book_file.readline()

    while current_line:
        pass


def get_non_chars():
    non_chars = {chr(i) for i in range(32,65)}
    non_chars.discard('-')
    return non_chars



def clean_line(line, stopwords, non_chars):
    # Split and strip:
    words = [word.strip() for word in clean_line.split()]

    # Get rid of

