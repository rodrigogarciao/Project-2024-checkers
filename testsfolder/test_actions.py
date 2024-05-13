def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

def is_winner(board, player):
    
    for row in board:
        for cell in row:
            if cell == switch_player(player):
                return False
    return True
print("IF this phrase prints it means that the code and the functions are well defined ")
 
           
   
