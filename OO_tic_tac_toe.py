def main() :
    board = Board()
    turn = 'X';
    playing = True;
    
    while(playing):
        board.print_me()
        print("It's your turn " + turn)
        x = int(input("x position? "))
        y = int(input("y position? "))
        board.place_checker(turn, x, y)
        if turn == 'X':
            turn = 'Y'
        else:
            turn = 'X'
     
main()

class Board:
    def __init__(self):
        self._layout = [['_', '_', '_'],
                        ['_', '_', '_'], 
                        ['_', '_', '_']]

    def print_me(self):
         for i in range(0, len(self._layout)):
            for j in range(0, len(self._layout[i])):
                print(board[i][j] + " ", end='')
            print()

    def place_checker(self, turn, x, y):
        self._layout[y][x] = turn;
