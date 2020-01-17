'''
Creates a game of tic tac toe
'''
#define the main function of the program
def main() :
    #create a board object
    board = Board()
    #set the first turn
    turn = 'X';
    playing = True;
    #repeats rounds of the game until no longer playing
    while(playing):
        #print the board
        board.print_me()
        #say who is playing and get their choice of move
        print("It's your turn " + turn)
        #get input from the player. Comes as text, so convert to number
        x = int(input("x position? "))
        y = int(input("y position? "))
        #change the board with a move
        board.place_checker(turn, x, y)
        #swap whose turn it is
        if turn == 'X':
            turn = 'Y'
        else:
            turn = 'X'

#call the main function     
main()

#define the board class
class Board:
    #initialize a board object. 'self' refers to the current object
    def __init__(self):
        #define an empty board layout 
        self._layout = [['_', '_', '_'],
                        ['_', '_', '_'], 
                        ['_', '_', '_']]

    #prints every board character in a nice format
    def print_me(self):
         #loop over every outer item in 2d list
         for i in range(0, len(self._layout)):
             #loop over inner items
            for j in range(0, len(self._layout[i])):
                #print on same line by setting end to blank
                print(board[i][j] + " ", end='')
            #print on the next line
            print()

    #change the board layout with a checker
    def place_checker(self, checker, x, y):
        self._layout[y][x] = checker;
