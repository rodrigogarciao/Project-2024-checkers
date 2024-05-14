def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

def test_switch_player():
    assert switch_player('X') == 'O'
    assert switch_player('O') == 'X'

    def make_move(board, start, end, player):
     start_row, start_col = start
    end_row, end_col = end

    board[start_row][start_col] = '_'
    board[end_row][end_col] = player


   
