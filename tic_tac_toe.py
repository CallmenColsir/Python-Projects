
player1 = "X"
player2 = "O"

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def boards(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    
def X_move(board,player1):
    while True:
        x_input = input("PlayerX enter position (1-9): ")
        if x_input.isdigit():
            if (int(x_input) > 0 and int(x_input) < 10 and board[int(x_input) - 1] == " "):
                board[int(x_input) - 1] = player1
                break
        else:
            pass
        
def O_move(board, player2):
    while True:
        o_input = input("PlayerO enter position (1-9): ")
        if o_input.isdigit():
            if (int(o_input) > 0 and int(o_input) < 10 and board[int(o_input) - 1] == " "):
                board[int(o_input) - 1] = player2
                break
        else:
            pass
        
class check_winner:
    def x_win(board):
        return (board[0] == board[1] == board[2] == player1 or
                board[3] == board[4] == board[5] == player1 or
                board[6] == board[7] == board[8] == player1 or
                board[0] == board[3] == board[6] == player1 or
                board[1] == board[4] == board[7] == player1 or
                board[2] == board[5] == board[8] == player1 or
                board[2] == board[4] == board[6] == player1 or
                board[0] == board[4] == board[8] == player1)
        
    def o_win(board):
        return (board[0] == board[1] == board[2] == player2 or
                board[3] == board[4] == board[5] == player2 or
                board[6] == board[7] == board[8] == player2 or
                board[0] == board[3] == board[6] == player2 or
                board[1] == board[4] == board[7] == player2 or
                board[2] == board[5] == board[8] == player2 or
                board[2] == board[4] == board[6] == player2 or
                board[0] == board[4] == board[8] == player2)
        
    def tie(board):
        return (" " not in board)
    
Winner = check_winner 
   
running = True
boards(board)
while running: 
    #game run

    X_move(board, player1)
    boards(board)
    
    # check winner
    if Winner.x_win(board):
        print("X win!")
        running = False

    elif Winner.tie(board):
        print("Tie game!")
        running = False
    else:
        O_move(board, player2)
        boards(board)
        if Winner.o_win(board):
            print("O win!")
            running = False

        
