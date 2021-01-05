import tkinter as tk

b_width = 5
b_height = 3
num1_populated = False
num2_populated = False
num1 = 0
num2 = 0
reset = False

def update_label(txt):
    global screen, reset
    if screen["text"] != "0" or txt == ".":
        if reset == False:
            txt = screen["text"] + txt
    screen.config(text=txt)
    reset = False


def update_operation(button):
    global screen, b_plus, b_minus, b_mul, b_div
    global num1, num2, num1_populated, num2_populated, reset
    buttons = [b_plus, b_minus, b_mul, b_div]
    if num1_populated == True and num2_populated == True:
        for btn in buttons:
            if btn["bg"] == "green":
                operation = button["text"]
        if operation == "+":
            num1 = num1 + num2
            b_plus.config(bg="silver")
        elif operation == "-":
            num1 = num1 - num2
            b_minus.config(bg="silver")
        elif operation == "X":
            num1 = num1 * num2
            b_mul.config(bg="silver")
        elif operation == "/":
            num1 = num1 / num2
            b_div.config(bg="silver")
        screen.config(text=str(num1))
        reset = True
        num1 = 0
        num2 = 0
        num1_populated = False
        num2_populated = False
    elif num1_populated == True and num2_populated == False:
        num2 = float(screen["text"])
        num2_populated = True
        update_result()
    if num1_populated == False and num2_populated == False or screen["text"] != "0":
        num1 = float(screen["text"])
        num1_populated = True
        screen.config(text="0")
        button.config(bg="green")
    

def update_result():
    global screen, b_plus, b_minus, b_mul, b_div
    global num1, num2, num1_populated, num2_populated, reset
    buttons = [b_plus, b_minus, b_mul, b_div]
    if num1_populated == True and num2_populated == True:
        for button in buttons:
            if button["bg"] == "green":
                operation = button["text"]
        if operation == "+":
            num1 = num1 + num2
            b_plus.config(bg="silver")
        elif operation == "-":
            num1 = num1 - num2
            b_minus.config(bg="silver")
        elif operation == "X":
            num1 = num1 * num2
            b_mul.config(bg="silver")
        elif operation == "/":
            num1 = num1 / num2
            b_div.config(bg="silver")
        screen.config(text=str(num1))
        reset = True
        num1 = 0
        num2 = 0
        num1_populated = False
        num2_populated = False
    elif num1_populated == True and num2_populated == False:
        num2 = float(screen["text"])
        num2_populated = True
        update_result()



def main():

    global screen, b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9, b_9, b_dot, b_plus, b_minus, b_mul, b_div

    window = tk.Tk()
    window.title("Calculadora")
    
    screen = tk.Label(window, text="0", font=("Arial", 18), width=b_width * 4, anchor="e")
    screen.grid(row=0, column=0, columnspan=4)

    b_0 = tk.Button(window, text="0", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("0"))
    b_1 = tk.Button(window, text="1", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("1"))
    b_2 = tk.Button(window, text="2", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("2"))
    b_3 = tk.Button(window, text="3", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("3"))
    b_4 = tk.Button(window, text="4", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("4"))
    b_5 = tk.Button(window, text="5", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("5"))
    b_6 = tk.Button(window, text="6", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("6"))
    b_7 = tk.Button(window, text="7", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("7"))
    b_8 = tk.Button(window, text="8", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("8"))
    b_9 = tk.Button(window, text="9", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("9"))
    b_dot = tk.Button(window, text=".", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_label("."))
    b_equal = tk.Button(window, text="=", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_result())
    b_plus = tk.Button(window, text="+", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_operation(b_plus))
    b_minus = tk.Button(window, text="-", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_operation(b_minus))
    b_mul = tk.Button(window, text="X", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_operation(b_mul))
    b_div = tk.Button(window, text="/", font=("Arial", 18), width=b_width, height=3, bg="silver", command=lambda: update_operation(b_div))

    b_7.grid(row=1,column=0)
    b_8.grid(row=1,column=1)
    b_9.grid(row=1,column=2)
    b_4.grid(row=2,column=0)
    b_5.grid(row=2,column=1)
    b_6.grid(row=2,column=2)
    b_1.grid(row=3,column=0)
    b_2.grid(row=3,column=1)
    b_3.grid(row=3,column=2)
    b_0.grid(row=4,column=0)
    b_dot.grid(row=4,column=1)
    b_equal.grid(row=4,column=2)
    b_plus.grid(row=1,column=3)
    b_minus.grid(row=2,column=3)
    b_mul.grid(row=3,column=3)
    b_div.grid(row=4,column=3)

    window.mainloop()


main()
