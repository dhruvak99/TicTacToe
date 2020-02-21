board = [["","",""],["","",""],["","",""]]

#player class has two variables name and player symbol
class player:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol

def print_board(board):
    for li in board:
        print(li)

#this method is used to check which player has won
def chech_winner(symbol):
    result = False
    if board[0][0]==board[0][1]==board[0][2]==symbol:
        result = True
    elif board[1][0]==board[1][1]==board[1][2]==symbol:
        result=True
    elif board[2][0]==board[2][1]==board[2][2]==symbol:
        result=True
    elif board[0][0]==board[1][0]==board[2][0]==symbol:
        result=True
    elif board[0][1]==board[1][1]==board[2][1]==symbol:
        result=True
    elif board[0][2]==board[1][2]==board[2][2]==symbol:
        result=True
    elif board[0][0]==board[1][1]==board[2][2]==symbol:
        result=True
    elif board[0][2]==board[1][1]==board[2][0]==symbol:
        result=True
    return result

def PlaceSymbol(symbol):
    box = int(input("Enter the box number..\n"))
    if box == 1 :
        board[0][0] = symbol
    elif  box ==2:
        board[0][1] = symbol
    elif box == 3:
        board[0][2] = symbol
    elif  box ==4:
        board[1][0] = symbol
    elif box == 5:
        board[1][1] = symbol
    elif  box ==6:
        board[1][2] = symbol
    elif box == 7:
        board[2][0] =symbol
    elif  box ==8:
        board[2][1] =symbol
    else:
        board[2][2] = symbol

def boardfull(board):
    symbol = ['X','O']
    if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2] in symbol:
        return True

player1_symbol=""
player2_symbol=""

symbol = input("Enter player 1 symbol either 'X' or 'O'\n")

player1_symbol =symbol
if player1_symbol == 'X':
    player2_symbol = 'O'
if player1_symbol == 'O':
    player2_symbol = 'X'

print("player 1 symbol "+player1_symbol)
print("player 2 symbol "+player2_symbol)

player1 = player('1',player1_symbol)
player2 = player('2',player2_symbol)

first=input("Which player goes first:\n")
if first == '1':
    goes_first=player1
    goes_second= player2
else:
    goes_first=player2
    goes_second=player1

print_board(board)

won_game = True
while(won_game):
    PlaceSymbol(goes_first.symbol)
    print_board(board)
    result1 =chech_winner(goes_first.symbol)
    PlaceSymbol(goes_second.symbol)
    print_board(board)
    result2 = chech_winner(goes_second.symbol)
    if result1==True:
        print(goes_first.name+" has won")
        won_game=False
    elif result2==True:
        print(goes_second.name+" has won")
        won_game=False
    elif boardfull(board):
        print("Draw match")
        won_game=False
    else:
        continue
