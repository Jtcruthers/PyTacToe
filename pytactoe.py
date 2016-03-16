# Justin Carruthers
# PyTacToe - A tic tac toe game written in Python
import random
import os

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
def isPlayerFirst():
    return True if random.randrange(2) == 1 else False

# Returns the index of the computer's move
def AIMoveFirst(board, computerLetter, playerLetter):

    move = whichMove(board)

    if board[4] == ' ':
        return 4

    elif board[4] != ' ' and move == 2:
        return 0

    # Check if we have 2 spots in a row
    canWinGame, emptySpot = determineGameCanEnd(board, computerLetter)
    if canWinGame == True:
        return emptySpot

    # Check if they have 2 spots in a row
    canLoseGame, emptySpot = determineGameCanEnd(board, playerLetter)
    if canLoseGame == True:
        return emptySpot

    # Pick opposite corner from player's move
    if move == 3:
        if board[0] == playerLetter or board[1] == playerLetter:
            return 8
        elif board[2] == playerLetter:
            return 6
        elif board[3] == playerLetter or board[6] == playerLetter or board[7] == playerLetter:
            return 2
        elif board[8] == playerLetter or board[5] == playerLetter:
            return 0

    # We know that the player has a corner piece and a mystery piece on a non-corner edge
    if move == 5:
        if board[1] == playerLetter:
            if board[6] == playerLetter:
                return 8
            else:
                return 6
        if board[3] == playerLetter:
            if board[8] == playerLetter:
                return 2
            else:
                return 8
        if board[5] == playerLetter:
            if board[0] == playerLetter:
                return 6
            else:
                return 0
        else:
            if board[2] == playerLetter:
                return 0
            else:
                return 2

    # Loop until get an empty spot
    while True:
        move = random.randrange(9)
        if board[move] == ' ':
            return move

# Checks to see if there are two spots filled with given letter, while the third spot is empty. If so, it returns the empty spot
def determineGameCanEnd(board, letter):
    indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (6, 4, 2), (0, 4, 8)]
    for indexSet in indices:
        canWinCombo, emptySpot = canEndWithCombo(indexSet, board, letter)
        if canWinCombo == True:
            return True, indexSet[emptySpot]

    return False, -1

# Checks if the game can end given a certain set of board squares.
def canEndWithCombo(indices, board, letter):
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
        if (userInput == "tl" or userInput == "0") and board[0] == ' ':
            return 0
        if (userInput == "tm"  or userInput == "1") and board[1] == ' ':
            return 1
        if (userInput == "tr"  or userInput == "2") and board[2] == ' ':
            return 2
        if (userInput == "ml"  or userInput == "3") and board[3] == ' ':
            return 3
        if (userInput == "mm"  or userInput == "4") and board[4] == ' ':
            return 4
        if (userInput == "mr"  or userInput == "5") and board[5] == ' ':
            return 5
        if (userInput == "bl"  or userInput == "6") and board[6] == ' ':
            return 6
        if (userInput == "bm"  or userInput == "7") and board[7] == ' ':
            return 7
        if (userInput == "br"  or userInput == "8") and board[8] == ' ':
            return 8
        print("Not a valid choice")

def checkWinningCombination(combination):
    return (True, combination[0]) if combination[0] != ' ' and combination[0] == combination[1] == combination[2] else (False, ' ')

def checkForWin(board):
    combinations = [(board[0], board[1], board[2]), (board[3], board[4], board[5]), (board[6], board[7], board[8]), (board[0], board[3], board[6]), (board[1], board[4], board[7]), (board[2], board[5], board[8]), (board[6], board[4], board[2]), (board[0], board[4], board[8])]
    for combo in combinations:
        didComboWin, winningLetter = checkWinningCombination(combo)
        if didComboWin == True:
            return True, winningLetter

    return False, ' '

# Returns true if there is a tie
def isATie(board):
    for square in board:
        if square == ' ':
            return False

    return True

# Returns which move we are on. First time anyone moves is the first move
def whichMove(board):
    count = 1
    for square in board:
        if square != ' ':
            count = count + 1

    return count

def AITurn(board, computerLetter, playerLetter):
    print("Computer's move")
    AIMoveIndex = AIMoveFirst(board, computerLetter, playerLetter)
    board[AIMoveIndex] = computerLetter

def playerTurn(board, playerLetter):
    userMoveIndex = getUserMove(board)
    board[userMoveIndex] = playerLetter


#The main loop of the game
def play():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    computerLetter = 'X'
    playerLetter = 'O'

    playerIsFirst = isPlayerFirst()
    os.system('clear')

    printBoard(board)
    if playerIsFirst == True:
        print("You go first!")
        print("You are " + playerLetter + "!\n")
    else:
        print("Computer goes first!")
        print("The computer is " + computerLetter + "!\n")

    while True:
        if playerIsFirst == True:
            playerTurn(board, playerLetter)
        else:
            os.system('clear')
            AITurn(board, computerLetter, playerLetter)

        printBoard(board)

        someoneWon, winningLetter = checkForWin(board)
        if someoneWon == True:
            if winningLetter == playerLetter:
                print("Congratulations! You won!")
            else:
                print("You lose.")
            break

        if isATie(board) == True: #Since there are 9 spots, there can only be a tie after the first person goes
            print("Tie!")
            break

        if playerIsFirst == True:
            AITurn(board, computerLetter, playerLetter)
        else:
            playerTurn(board, playerLetter)

        printBoard(board)

        someoneWon, winningLetter = checkForWin(board)
        if someoneWon == True:
            if winningLetter == playerLetter:
                print("Congratulations! You won!")
            else:
                print("You lose.")
            break

print("Welcome to Tic-Tac-Toe!\n")
play()

