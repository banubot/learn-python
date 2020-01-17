'''
Creates a game of tic tac toe
'''

#define the main function
def main() :
    #make a list of empty board spots using _ character 
    #and assign it to a variable named board
    board = [['_', '_', '_'],
             ['_', '_', '_'], 
             ['_', '_', '_']]
   
    #set the first player as X
    turn = 'X';
    #make a variable to decide if we're still playing
    playing = True;
    
    #loop ove a round of the game until we aren't playing anymore
    while(playing):
        #call a function to display the board
        print_board(board)
        #tell the user whose turn it is
        print("It's your turn " + turn)
        #ask the user for x and y positions and grab their response.
        #the response comes back as a string of characters, 
        #so convert it to an integer
        x = int(input("x position? "))
        y = int(input("y position? "))
        #change the board at position (x,y) to be the checker
        #of this player
        board[y][x] = turn;
        #swap which player's turn it is
        if turn == 'X':
            turn = 'Y'
        else:
            turn = 'X'

#defines a function to print the board in a pretty format
def print_board(board):
    #loop from zero to the length of the board in 1 dimension
    #(outer elements)
    for i in range(0, len(board)):
        #loop over the other dimension (inner elements)
        for j in range(0, len(board[i])):
            #display the character in one postion 
            #set the ending character as blank to
            #print on one line
            print(board[i][j] + " ", end='')
        #print on the next line
        print()

main()
