def main() :
    board = [['_', '_', '_'],
             ['_', '_', '_'], 
             ['_', '_', '_']]
   
    turn = 'X';
    playing = True;
    
    while(playing):
        print_board(board)
        print("It's your turn " + turn)
        x = int(input("x position? "))
        y = int(input("y position? "))
        board[y][x] = turn;
        if turn == 'X':
            turn = 'Y'
        else:
            turn = 'X'
     
def print_board(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            print(board[i][j] + " ", end='')
        print()

main()
