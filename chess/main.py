from piece import *
from board_setup import *


# Initialize and print the board
chess_board = initialize_board()
print_board(chess_board)

# Player is asked to choose his moves
piece_to_move=input("choose the piece you want to move"'\n')
new_piece_position=input("choose the destination of the piece"'\n')
piece_to_move=chess_coord_to_index(piece_to_move)
new_piece_position=chess_coord_to_index(new_piece_position)


print(piece_to_move,new_piece_position)
