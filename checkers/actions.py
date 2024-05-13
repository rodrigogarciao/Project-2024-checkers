def is_valid_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < 8 and 0 <= start_col < 8):
        return False

    if not (0 <= end_row < 8 and 0 <= end_col < 8):
        return False

    if board[end_row][end_col] != '_':
        return False
# The function here it works so that the movement can get located in the board while the player is doing it with the coordiantes that where given at the beggining

  
    if player == 'X':
        if end_row < start_row or abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
            return False
    elif player == 'O':
        if end_row > start_row or abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
            return False
    
    return True

def make_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end


    board[start_row][start_col] = '_'
    board[end_row][end_col] = player

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'
#The function previously mentioned in what point we need to make te change of player and if the movement can`t be done retunr to the same player until it makes a movement which can be choosed 
def is_winner(board, player):
    
    for row in board:
        for cell in row:
            if cell == switch_player(player):
                return False
    return True


def make_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end


    board[start_row][start_col] = '_'
    board[end_row][end_col] = player
    def is_valid_move(board, start, end, player):
        start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < 8 and 0 <= start_col < 8):
        return False

    if not (0 <= end_row < 8 and 0 <= end_col < 8):
        return False

    if board[end_row][end_col] != '_':
        return False

  
    if player == 'X':
        if end_row < start_row or abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
            return False
    elif player == 'O':
        if end_row > start_row or abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
            return False
    
    return True

def make_move(board, start, end, player):
    start_row, start_col = start
    end_row, end_col = end


    board[start_row][start_col] = '_'
    board[end_row][end_col] = player

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
print("The other player can`t make any more moves you win")