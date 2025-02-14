#from tkinter import Tk, Button, StringVar, Entry
from functools import partial  #works like lambda (sort of)
from customtkinter import CTk, CTkEntry, CTkButton, StringVar  #visually better Tk
import math
from math import sqrt

"""
    Main idea: make fancy calculator
    Do it in object oriented style

    Basic operations: +, -, *, /, sqrt(), negation, adding ',' (float), =

    GUI for calculator (Tkinter)
    
    If free time:
        Make custom pixel(?) graphics
        
    How works:
    Take input from buttons (0-9), Store that data, do calculations, do until user quits and print final answer on CLI
"""
expression = ""  #global variable for holding result


class Window(CTk):
    """
    Settings of main window like layout of buttons, functions
    """

    def __init__(self):
        super().__init__()  # inheritance from Tk

        #Window settings
        self.title("Calculator")
        self.configure(background="light green")
        self.geometry("300x300")

        self.buttons = []  #list for buttons

        buttonValues = [  #add any button you need ("ButtonValue", column, row)
            (1, 0, 1), (2, 1, 1), (3, 2, 1), ('Clear', 3, 1), ('<-', 4, 1),
            (4, 0, 2), (5, 1, 2), (6, 2, 2), ('+', 3, 2), ('-', 4, 2),
            (7, 0, 3), (8, 1, 3), (9, 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('+/-', 0, 4), (0, 1, 4), (',', 2, 4), ('√', 3, 4), ('=', 4, 4),
        ]
        self.operations = {
            "clear": clear,
            "+": add,
            "-": substract,
            "*": multiply,
            "/": divide,
            "+/-": negation,
            ",": floatNum,
            "√": sqrt,
            "=": equal,
            "<-": backspace,

        }
        #cols and rows are for making grid even
        for col in range(5):
            self.grid_columnconfigure(col, weight=1)
        for row in range(5):
            self.grid_rowconfigure(row, weight=1)

        #buttons are added to grid and to list of buttons
        for num, col, row in buttonValues:
            button = CTkButton(self, text=str(num), bg_color="green", width=10, height=1,
                               command=partial(press, num))  #partial remembers to value to func
            button.grid(column=col, row=row, padx=20, pady=20)
            self.buttons.append(button)


def press(num):
    global expression
    if expression == "0":  # deletes first 0 (so we don't have something like 06, just 6)
        expression = ""
    if isinstance(num, str):  #checks if num is a string
        num = num.lower()  #lowers the first digit
        for key, value in window.operations.items():  #searches for function
            if key == num:
                resultFunction = window.operations[num]
                resultFunction()  #uses function
    else:

        expression = expression + str(num)
        textBox.set(expression)
        print(expression)


def add():
    global expression
    expression = expression + "+"
    textBox.set(expression)


def substract():
    global expression

    expression = expression + "-"
    textBox.set(expression)


def multiply():
    global expression

    expression = expression + "*"
    textBox.set(expression)


def divide(): #divides the number
    global expression

    expression = expression + "/"
    textBox.set(expression)


def negation(): #negation of number
    global expression

    print(expression[0])
    if expression[0] == "-":
        expression = expression[1:]
    else:
        expression = "-" + expression
    textBox.set(expression)


def sqrt():  #square root
    global expression
    expression = "math.sqrt(" + expression + ")"
    textBox.set(expression)


def floatNum():
    global expression
    expression = expression + ",0"
    textBox.set(expression)


def clear():  #clears the display
    global expression
    expression = "0"
    textBox.set(expression)


def backspace():  #deletes one letter from the end
    global expression
    expression = expression[:-1]
    textBox.set(expression)


def equal():  #show the sum of the numbers
    global expression

    while expression.count("(") > expression.count(")"):
        expression += ")"
    try:
        # Pozwalamy eval używać wszystkich funkcji z math
        result = eval(expression, {"__builtins__": None}, math.__dict__)

        textBox.set(str(result))  # Wyświetlamy wynik
        expression = str(result)  # Zapisujemy nowy wynik jako expression
    except Exception as e:
        textBox.set("Error")  # Obsługa błędów (np. dzielenie przez 0)
        expression = ""



window = Window()

textBox = StringVar()  #text were value of result is displayed
textBox.set("0")  #default value

#field where result is displayed
expressionField = CTkEntry(window, textvariable=textBox, font=('arial', 18, 'bold'))
expressionField.grid(columnspan=5, column=0, row=0, ipadx=90, ipady=10)

print("ok")

#starts the program
window.mainloop()
