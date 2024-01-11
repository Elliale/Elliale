def initialize_board():
    # Create an 8x8 array of spaces
    board = [[" " for _ in range(8)] for _ in range(8)]

    # Set up the black pieces
    board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    board[1] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']

    # Set up the white pieces
    board[6] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']

    return board

def print_board(board):
    # Print column indices
    print("  A B C D E F G H")

    # Print the board with row indices
    row_number = 8
    for row in board:
        print(f"{row_number} {' '.join(row)}")
        row_number -= 1

#change coordonate like "A8" into board coordonate [7,0]
def chess_coord_to_index(coord):
    col = ord(coord[0].upper()) - ord('A')
    row = 8 - int(coord[1])
    return row, col

#color attribution of pieces
def color_attribution(piece):
    