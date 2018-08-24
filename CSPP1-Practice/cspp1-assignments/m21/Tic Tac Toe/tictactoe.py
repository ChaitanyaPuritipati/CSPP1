class Tictactoe(object):
    def __init__(self, board):
        self.board = board
    def __reset__(self):
        self.board = [['_','_','_'],['_','_','_'],['_','_','_']] 
    def update_board(self, position_1,position_2, value, index):
        try:
            if self.board[position_1][position_2] is '_':
                self.board[position_1][position_2] = value
            else:
                raise Exception("Already Present")
        except:
            print("Invalid Input or Already Present")
            if index == 1:
                player_1_input = input("Give Input for Player"+str(index)+" again: ").split()
                Tictactoe.update_board(self, int(player_1_input[0]),int(player_1_input[1]), "X", 1)
            if index == 2:
                player_2_input = input("Give Input for Player"+str(index)+" again: ").split()
                Tictactoe.update_board(self, int(player_2_input[0]),int(player_2_input[1]), "O", 2)    
    def get_board(self):
        return self.board
    def check_rows(self):
        out_lst =[]
        if set(self.board[0]) == {'x'} or set(self.board[1]) == {'x'} or set(self.board[2]) == {'x'}: 
            out_lst.append('x')
        if set(self.board[0]) == {'o'} or set(self.board[1]) == {'o'} or set(self.board[2]) == {'o'}:
            out_lst.append('o')
        if len(out_lst) > 1:
            return False
        if len(out_lst) == 1:    
            return out_lst[0]    
    def check_columns(self):
        out_lst = []
        if set([self.board[0][0],self.board[1][0], self.board[2][0]]) == {'x'} \
        or set([self.board[0][1],self.board[1][1],self.board[2][1]]) == {'x'} \
        or set([self.board[0][2],self.board[1][2], self.board[2][2]]) == {'x'}:
            out_lst.append('x') 
        
        if set([self.board[0][0],self.board[1][0], self.board[2][0]]) == {'o'} \
        or set([self.board[0][1],self.board[1][1], self.board[2][1]]) == {'o'} \
        or set([self.board[0][2],self.board[1][2], self.board[2][2]]) == {'o'}:
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
                #return True
        return 0                   

#board = [['_','_','_'],['_','_','_'],['_','_','_']]
def main():
    board = []
    for i in range(3):
        board.append(input().split()) 
    game = Tictactoe(board)
    if game.board_check() == 1:
        return "invalid input"
    if game.check_rows() == False or game.check_columns() == False or game.check_diagonals() == False :
        return "1 invalid game"    
    if (game.check_rows() == game.check_columns()) and (game.check_columns() == game.check_diagonals()):
        return "2 invalid game"
    if  (game.check_rows() == game.check_columns()) or (game.check_columns() == game.check_diagonals()) or (game.check_rows() == game.check_diagonals()):
        return "3 invalid game"    
    
    #def displayboard(board):
        #for i in board:
            #for j in i:
                #print(j," ", end="")
            #print()
    #displayboard(board) 
    #while True:
        #player_1_input = input("Player 1 input enter here: ").split()
        #game.update_board(int(player_1_input[0]), int(player_1_input[1]), "X", 1)
        #board_print = game.get_board()
        #displayboard(board_print)
        #print(board_print)
        #if game.check_rows() == True or game.check_columns() == True or game.check_diagonals() == True:
            #print("Player 1 wins")
            #break
        #if game.board_check() == False:
            #print("Game Over! Ran out of chances")
            #reset_input = input("Enter Y to create a new board and start the game again: ")
            #if reset_input == 'Y' or reset_input == 'y':
                #game.__reset__()
            #else:
                #print("Thanks for playing the game!")
                #break  
        #player_2_input = input("Player 2 input enter here: ").split()
        #game.update_board(int(player_2_input[0]), int(player_2_input[1]), "O", 2)
        #board_print = game.get_board()
        #print(board_print)
        #displayboard(board_print)
        #if game.check_rows() == True or game.check_columns() == True or game.check_diagonals() == True:
            #print("Player 2 wins")
            #break
        #if game.board_check() == False:
            #print("Game Over! Ran out of chances")
            #reset_input = input("Enter Y to create a new board and start the game again: ")
            #if reset_input == 'Y' or reset_input == 'y':
                #game.__reset__()
            #else:
                #print("Thanks for Playing the game!")
                #break
if __name__ == '__main__':
            print(main())          
