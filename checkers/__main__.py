from board import new_board, print_board
from actions import switch_player, is_winner, is_valid_move, make_move

board = new_board()
player1 = 'X'
player2 = 'O'
current_player = player1

from board import new_board, print_board
from actions import is_winner, is_valid_move, make_move, switch_player

board = new_board()
current_player = 'X'

print("Enter positions in the format 'row,col'. For example, '3,4' represents row 3, column 4.")

while not is_winner(board, current_player):
    print_board(board)
    
    start = input(f"Player {current_player}, enter start position (row, col): ").split(',')
    start = tuple(map(int, start))
    end = input(f"Player {current_player}, enter end position (row, col): ").split(',')
    end = tuple(map(int, end))
    
    if is_valid_move(board, start, end, current_player):
        make_move(board, start, end, current_player)
        current_player = switch_player(current_player)
    else:
        print("Thats incorrect, try again")

print_board(board)
print(f"Player {current_player} wins by so much!")


