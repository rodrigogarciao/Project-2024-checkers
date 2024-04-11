def _(new_board):
    # Defining the board 
    checkers.board = [
        ['_', 'X', '_', 'X', '_', 'X', '_', 'X'],
        ['X', '_', 'X', '_', 'X', '_', 'X', '_'],
        ['_', 'X', '_', 'X', '_', 'X', '_', 'X'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['O', '_', 'O', '_', 'O', '_', 'O', '_'],
        ['_', 'O', '_', 'O', '_', 'O', '_', 'O'],
        ['O', '_', 'O', '_', 'O', '_', 'O', '_']
    ]

def print_board(checkers):
    for row in checkers.board:
        print(' '.join(row))

        
