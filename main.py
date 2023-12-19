import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

currentPlayer = "X"
winner = None
gameRunning = True


# printing the game board
def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print("------------")
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print("------------")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')


# take player input
def playerInput(board):
    number_input = int(input('Please select a number between 1-9:'))
    if 9 > number_input < 0:
        print('Please select a number in between 1-9')
    if number_input >= 1 and number_input <= 9 and board[number_input - 1] == "-":
        board[number_input - 1] = currentPlayer
    else:
        print('Whoops. Another player is already in that spot!')


def compMove(board):
    while currentPlayer == "O":
        pos = random.randint(0,8)
        if board[pos] == "-":
            board[pos] = "0"
            switchPlayer()


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning = False


def checkForWin(board):
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiag(board):
        print(f"{currentPlayer} is the winner!")
        printBoard(board)
        gameRunning = False

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# check for win or tie again


# run
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkForWin(board)
    checkTie(board)
    switchPlayer()
    compMove(board)
    checkForWin(board)
    checkTie(board)