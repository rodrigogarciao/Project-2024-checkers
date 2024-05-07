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




