from checkers.actions import is_valid_move, make_move, switch_player
from checkers.board import new_board


def test_is_valid_move(self):
        board = new_board()
        start = (2, 1)
        end = (3, 2)
        self.assertTrue(is_valid_move(board, start, end, 'X'))
 
    
def test_make_move(self):
        board = new_board()
        start = (2, 1)
        end = (3, 2)
        make_move(board, start, end, 'X')
        self.assertEqual(board[2][1], '_')
        self.assertEqual(board[3][2], 'X')

def test_switch_player(self):
        player1 = 'X'
        player2 = 'O'
        self.assertEqual(switch_player(player1), player2)
        self.assertEqual(switch_player(player2), player1)

    
 
           
   
