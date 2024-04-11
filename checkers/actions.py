 # PLayers
checkers.player1 = 'X'  
checkers.player2 = 'O'  
checkers.current_player = checkers.player1  

def print_board(checkers):
    for row in checkers.board:
        print(' '.join(row))

def is_valid_move(checkers, start, end):
    # See if that move can be done 
    pass

def make_move(checkers, start, end):
    # How to get the movement made 
    pass

def switch_player(checkers):
    # Switch Player
    if checkers.current_player == checkers.player1:
        checkers.current_player = checkers.player2
    else:
        checkers.current_player = checkers.player1

def is_winner(checkers):
       
        

    game = CheckersGame()
game.print_board()