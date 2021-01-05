import random

board = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]


def board_print(board):
    print()
    print("---------------")
    for line in board:
        print(f" | {line[0]} | {line[1]} | {line[2]} |")
        print("---------------")
    print()


def board_write(board, letter):
    line = int(input("Enter the line number: ")) - 1
    column = int(input("Enter the column number: ")) - 1
    if board[line][column] == '-':
        board[line][column] = letter
        return True
    return False

def board_computer_write(board, letter):
    searching = True
    while searching:
        line = random.randint(0,2)
        column = random.randint(0,2)
        if board[line][column] == '-':
            board[line][column] = letter
            searching = False


def board_check(board):
    draw = True
    for line in board:
        if line[0] == line[1] and line[0] == line[2] and line[0] != '-':
            return line[0]
    for i in range(0,3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '-':
            return board[0][i]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][0] != '-':
        return board[0][2]
    for line in board:
        for letter in line:
            if letter == '-':
                draw = False
                break
    if draw:
        return "Draw"
    return '-'


def game(board):
    turn = 'X'
    result = '-'
    print("Lets play Tic Tac Toe, you will play against the computer")
    while result == '-':
        board_print(board)
        if turn == 'X':
            board_write(board, turn)
            turn = 'O'
        else:
            board_computer_write(board, turn)
            turn = 'X'
        result = board_check(board)
    if result == "Draw":
        print("It was a Draw!")
        board_print(board)
    else:
        print(f"The winner is {result}")
        board_print(board)


game(board)
