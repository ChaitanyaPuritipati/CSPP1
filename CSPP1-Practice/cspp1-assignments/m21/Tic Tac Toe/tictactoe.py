class Tictactoe(object):
    def __init__(self, board):
        self.board = board
    def check_rows(self):
        out_lst = []
        if set(self.board[0]) == {'x'} or set(self.board[1]) == {'x'} \
        or set(self.board[2]) == {'x'}:
            out_lst.append('x')
        if set(self.board[0]) == {'o'} or set(self.board[1]) == {'o'} \
        or set(self.board[2]) == {'o'}:
            out_lst.append('o')
        if len(out_lst) > 1:
            return False
        if len(out_lst) == 1:
            return out_lst[0]
    def check_columns(self):
        out_lst = []
        if set([self.board[0][0], self.board[1][0], self.board[2][0]]) == {'x'} \
        or set([self.board[0][1], self.board[1][1], self.board[2][1]]) == {'x'} \
        or set([self.board[0][2], self.board[1][2], self.board[2][2]]) == {'x'}:
            out_lst.append('x')
        if set([self.board[0][0], self.board[1][0], self.board[2][0]]) == {'o'} \
        or set([self.board[0][1], self.board[1][1], self.board[2][1]]) == {'o'} \
        or set([self.board[0][2], self.board[1][2], self.board[2][2]]) == {'o'}:
            out_lst.append('o')
        if len(out_lst) > 1:
            return False
        if len(out_lst) == 1:
            return out_lst[0]
    def check_diagonals(self):
        out_lst = []
        if set([self.board[0][0], self.board[1][1], self.board[2][2]]) == {'x'}\
        or set([self.board[0][2], self.board[1][1], self.board[2][0]]) == {'x'}:
            out_lst.append('x')
        if set([self.board[0][0], self.board[1][1], self.board[2][2]]) == {'o'}\
        or set([self.board[0][2], self.board[1][1], self.board[2][0]]) == {'o'}:
            out_lst.append('o')
        if len(out_lst) > 1:
            return False
        if len(out_lst) == 1:
            return out_lst[0]
    def board_check(self):
        check = 0
        for ele in self.board:
            check = check + ele.count('.') + ele.count('x') + ele.count('o')
        if check != 9:
            return 1
        return 0
def main():
    board = []
    for i in range(3):
        board.append(input().split())
    game = Tictactoe(board)
    invalid_flag = False
    if game.board_check() == 1:
        return "invalid input"
    if set([game.check_columns(), game.check_diagonals(), game.check_rows()]) == {None}:
        return "draw"
    if (game.check_rows() == 'x' or game.check_rows() == 'o') and \
    (set([game.check_columns(), game.check_diagonals()]) == {None}):
        return game.check_rows()
    if (game.check_columns() == 'x' or game.check_columns() == 'o') and \
    (set([game.check_rows(), game.check_diagonals()]) == {None}):
        return game.check_columns()
    if (game.check_diagonals() == 'x' or game.check_diagonals() == 'o') and \
    (set([game.check_columns(), game.check_rows()]) == {None}):
        return game.check_diagonals() 
    if game.check_rows() is False or game.check_columns() is False or \
    game.check_diagonals() is False :
        invalid_flag = True
    if (game.check_rows() == game.check_columns()) and \
    (game.check_columns() == game.check_diagonals()):
        invalid_flag = True
    if  (game.check_rows() == game.check_columns()) or \
    (game.check_columns() == game.check_diagonals()) or \
    (game.check_rows() == game.check_diagonals()):
        invalid_flag = True
    if invalid_flag == True:
        return "invalid game"
if __name__ == '__main__':
    print(main())
