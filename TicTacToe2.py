from tkinter import *
from tkinter import messagebox

turn = 'X'
board = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]


def reset():
    global board, turn
    turn = 'X'
    board = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]
    for button in buttons:
        button.config(text='-')
        button.config(bg="silver")
        button.config(state=NORMAL)

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

def win_state(status):
    for button in buttons:
        button.config(state=DISABLED)
        if button["text"] == status:
            button.config(bg="green")
        else:
            button.config(bg="gray")
    if status == "Draw":
        messagebox.showinfo("TicTacToe", "We have a Draw!!!")
    else:
        messagebox.showinfo("TicTacToe", "We have a Winner!!!")

def board_write(board, y, x, button):
    global turn
    if board[y][x] == '-':
        board[y][x] = turn
        button.config(text=turn)
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
    else:
        messagebox.showerror("TicTacToe", "Space not available")
    status = board_check(board)
    if status != '-':
        win_state(status)


window = Tk()
window.title("TicTacToe")

b1 = Button(window, text=board[0][0], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 0, 0, b1))
b2 = Button(window, text=board[0][1], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 0, 1, b2))
b3 = Button(window, text=board[0][2], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 0, 2, b3))
b4 = Button(window, text=board[1][0], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 1, 0, b4))
b5 = Button(window, text=board[1][1], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 1, 1, b5))
b6 = Button(window, text=board[1][2], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 1, 2, b6))
b7 = Button(window, text=board[2][0], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 2, 0, b7))
b8 = Button(window, text=board[2][1], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 2, 1, b8))
b9 = Button(window, text=board[2][2], font=("Helvetica", 20), height=3, width=6, bg="silver", command=lambda: board_write(board, 2, 2, b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

buttons = (b1, b2, b3, b4, b5, b6, b7, b8, b9)

b_reset = Button(window, text="Reset Game", font=("Helvetica", 12), command=lambda: reset())

b_reset.grid(row=3, column=0)

window.mainloop()