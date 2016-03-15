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
def AIMove(board, computerLetter, playerLetter):
    if board[4] == ' ':
        return 4
    #Check if we have 2 spots in a row
    canWinGame, emptySpot = determineCanWinGame(board, computerLetter)
    if canWinGame == True:
        return emptySpot
    #Check if they have 2 spots in a row
    canLoseGame, emptySpot = determineCanWinGame(board, playerLetter)
    if canLoseGame == True:
        return emptySpot
    isNonCornerOpen, spot = nonCornerIsOpen(board)
    if isNonCornerOpen == True:
        return spot

    #Loop until get an empty spot
    while True:
        move = random.randrange(9)
        if board[move] == ' ':
            return move

#Checks to see if there are two spots filled with AI letter with the third spot empty. If so, it returns the empty spot
def determineCanWinGame(board, letter):
    indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (6, 4, 2), (0, 4, 8)]
    for indexSet in indices:
        canWinCombo, emptySpot = canWinWithCombo(indexSet, board, letter)
        if canWinCombo == True:
            return True, indexSet[emptySpot] 

    return False, -1

def canWinWithCombo(indices, board, letter):
    combo = board[indices[0]], board[indices[1]], board[indices[2]]
    if combo[0] == letter and combo[1] == letter and combo[2] == ' ':
        return True, 2
    if combo[1] == letter and combo[2] == letter and combo[0] == ' ':
        return True, 0
    if combo[0] == letter and combo[2] == letter and combo[1] == ' ':
        return True, 1

    else:
        return False, -1

# If a non-corner, non-middle spot is open, it returns true and the index
def nonCornerIsOpen(board):
    if board[1] == ' ':
        return True, 1
    elif board[7] == ' ':
        return True, 7
    elif board[3] == ' ':
        return True, 3
    elif board[5] == ' ':
        return True, 5
    else:
        return False, -1

# Returns the index of the user move
def getUserMove(board):
    while True:
        userInput = input("Enter your move choice: ")
        if userInput == "tl" and board[0] == ' ':
            return 0
        if userInput == "tm"and board[1] == ' ':
            return 1
        if userInput == "tr" and board[2] == ' ':
            return 2
        if userInput == "ml" and board[3] == ' ':
            return 3
        if userInput == "mm" and board[4] == ' ':
            return 4
        if userInput == "mr" and board[5] == ' ':
            return 5
        if userInput == "bl" and board[6] == ' ':
            return 6
        if userInput == "bm" and board[7] == ' ':
            return 7
        if userInput == "br" and board[8] == ' ':
            return 8
        print("Not a valid choice")

def checkWinningCombination(combination):
    return True if combination[0] != ' ' and combination[0] == combination[1] == combination[2] else False 
         
def checkForWin(board):
    combinations = [(board[0], board[1], board[2]), (board[3], board[4], board[5]), (board[6], board[7], board[8]), (board[0], board[3], board[6]), (board[1], board[4], board[7]), (board[2], board[5], board[8]), (board[6], board[4], board[2]), (board[0], board[4], board[8])]
    for combo in combinations:
        if checkWinningCombination(combo) == True:
            return True

    return False

# Returns true if there is a tie
def isATie(board):
    for square in board:
        if square == ' ':
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
        print("Computer's move")
        AIMoveIndex = AIMove(board, computerLetter, userLetter)
        board[AIMoveIndex] = computerLetter
        printBoard(board)

        someoneWon = checkForWin(board)
        if someoneWon == True:
            printLoser()
            break
        if isATie(board) == True: #Since there are 9 spots, there can only be a tie after the first person goes
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

