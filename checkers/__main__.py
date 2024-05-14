
from board import new_board, print_board
from actions import is_winner, is_valid_move, make_move, switch_player

board = new_board()
current_player = 'X'
#Ginving Instruction
print("Welcome to Checkers!")
print("Checkers is a game that is played with 2 persons and in this case is the only way to play it ")
print("You can only do movements in diagonal and the point of this game is for you to eat the O or X that the player your going against is using ")
print("You win when you have eaten all the pieces or the other player can`t make any movementes anymore ")
print("Enter positions in the format 'row,col'. For example, '3,4' represents row 3, column 4.")

while not is_winner(board, current_player):
    print_board(board)
    
    start = input(f"Player {current_player}, enter start position (row, col): ").split(',')
    start = tuple(map(int, start))
    end = input(f"Player {current_player}, enter end position (row,3 col): ").split(',')
    end = tuple(map(int, end))
    
    if is_valid_move(board, start, end, current_player):
        make_move(board, start, end, current_player)
        current_player = switch_player(current_player)
    else:
        print("That's incorrect, try again")

print_board(board)
print(f"Player {current_player} wins! Congratulations!")


