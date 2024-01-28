board = [' ' for x in range(10)]
o_score = 0
x_score = 0


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter, so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def playerMove():
    run = True
    while run:
        move = input("Enter the position you want to place an X, (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is already occupied!")
            else:
                print("Please select a number in range")
        except:
            print("Please type a number")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    import random

    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def keepScore():
    global x_score
    global o_score
    if isWinner(board, 'X'):
        x_score += 1
    else:
        o_score += 1
    return x_score, o_score


def main():

    play = True
    print('Welcome to tictactoe')
    printBoard(board)

    while play:

        while not (isBoardFull(board)):
            if not (isWinner(board, 'O')):
                playerMove()
                printBoard(board)
            else:
                print('Sorry O\'s won this time')
                score = keepScore()
                print("X Score: ", score[0], "O Score: ", score[1])
                play = False
                break
            if not (isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    print("Tie game")
                else:
                    insertLetter('O', move)
                    print("Computer placed an O in position", move)
                    printBoard(board)
                compMove()
                printBoard(board)
            else:
                print('You won this time')
                break

        if isBoardFull(board):
            print('Tied game')
        else:
            break


while True:
    answer = input("Would you like to play tictactoe? (y/n)")
    if answer == "y":
        board = [' ' for x in range(10)]
        main()
    else:
        print("Final Score: ", "X Score:", x_score, "O Score:", o_score)
        break
