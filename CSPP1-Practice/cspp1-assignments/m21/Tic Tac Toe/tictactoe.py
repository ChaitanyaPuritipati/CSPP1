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
        if set(self.board[0]) == {'X'} or set(self.board[1]) == {'X'} or set(self.board[2]) == {'X'} or set(self.board[0]) == {'O'} or set(self.board[1]) == {'O'} or set(self.board[2]) == {'O'}:
            return True
        return False
    def check_columns(self):
        if set([self.board[0][0],self.board[1][0], self.board[2][0]]) == {'X'} \
        or set([self.board[0][1],self.board[1][1],self.board[2][1]]) == {'X'} \
        or set([self.board[0][2],self.board[1][2], self.board[2][2]]) == {'X'} \
        or set([self.board[0][0],self.board[1][0], self.board[2][0]]) == {'O'} \
        or set([self.board[0][1],self.board[1][1], self.board[2][1]]) == {'O'} \
        or set([self.board[0][2],self.board[1][2], self.board[2][2]]) == {'O'}:
            return True
        return False
    def check_diagonals(self):
        if set([self.board[0][0], self.board[1][1], self.board[2][2]]) == {'X'}\
        or set([self.board[0][2], self.board[1][1], self.board[2][0]]) == {'X'}\
        or set([self.board[0][0], self.board[1][1], self.board[2][2]]) == {'O'}\
        or set([self.board[0][2], self.board[1][1], self.board[2][0]]) == {'O'}:
            return True
        return False
    def board_check(self):
        for ele in self.board:
            if '_' in ele:
                return True
        return False                   

#board = [['_','_','_'],['_','_','_'],['_','_','_']]
board = []
for i in range(3):
	board.append(input()) 
print(board)
#game = Tictactoe(board)
#def displayboard(board):
    #for i in board:
        #for j in i:
            #print(j," ", end="")
        #print() 
#displayboard(board) 
# print(board)
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