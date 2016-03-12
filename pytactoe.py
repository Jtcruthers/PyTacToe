import random

def printBoard(board):
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |   ")
    print("")

# Returns true if user goes first, false if computer is
def whoFirst():
    return True if random.randrange(2) == 1 else False

        
# Returns the index of the computer's move
def AIMove(board):
    goodMove = False
    while goodMove == False:
        move = random.randrange(9)
        if board[move] == ' ':
            return move

def getUserMove(board):
    while True:
        userMoveIndex = int(input("Enter your move choice: "))
        if board[userMoveIndex] == ' ':
            return userMoveIndex 

def checkWinningCombination(combination):
    return True if combination[0] != ' ' and combination[0] == combination[1] == combination[2] else False 
         
def checkForWin(board):
    combinations = [(board[0], board[1], board[2]), (board[3], board[4], board[5]), (board[6], board[7], board[8]), (board[0], board[3], board[6]), (board[1], board[4], board[7]), (board[2], board[5], board[8]), (board[6], board[4], board[2]), (board[0], board[4], board[8])]
    for combo in combinations:
        if checkWinningCombination(combo) == True:
            return True

    return False

def checkForTie(board):
    for square in board:
        if board == ' ':
            return False

    return True

def printWinner():
    print("Congratulations! You won!") 

def printLoser():
    print("You lose.")


#The main loop of the game
def play():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    printBoard(board)
    computerLetter = 'X'
    userLetter = 'O'
    winningLetter = ' '

    someoneWon = False

    print(computerLetter + " goes first!\n")

    while True:
        AIMoveIndex = AIMove(board)
        board[AIMoveIndex] = computerLetter
        printBoard(board)

        someoneWon = checkForWin(board)
        if someoneWon == True:
            printLoser()
            break
        if checkForTie == True: #Since there are 9 spots, there can only be a tie after the first person goes
            print("Tie!")
            break

        userMoveIndex = getUserMove(board)
        board[userMoveIndex] = userLetter
        
        printBoard(board)
    
        someoneWon = checkForWin(board)
        if someoneWon == True:
            printWinner()
            break

        

print("Welcome to Tic-Tac-Toe!\n")
play()

