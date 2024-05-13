def new_board():
    board = [
        ['_', 'X', '_', 'X', '_', 'X', '_', 'X'],
        ['X', '_', 'X', '_', 'X', '_', 'X', '_'],
        ['_', 'X', '_', 'X', '_', 'X', '_', 'X'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['O', '_', 'O', '_', 'O', '_', 'O', '_'],
        ['_', 'O', '_', 'O', '_', 'O', '_', 'O'],
        ['O', '_', 'O', '_', 'O', '_', 'O', '_']
    ]
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

        
#Idea of the board got it from online link in the sourcs 