#from tkinter import Tk, Button, StringVar, Entry
import re
from functools import partial  #works like lambda (sort of)
from customtkinter import CTk, CTkEntry, CTkButton, StringVar, set_default_color_theme  #visually better Tk
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
expression = "0"  #global variable for holding result

set_default_color_theme("green")  #default color of CTkWindow

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
            "√": squareRoot,
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
            button = CTkButton(self, text=str(num), fg_color="green", width=35, height=15, hover_color="dark green",
                               command=partial(press, num), font=("arial", 15, 'bold'))  #partial remembers to value to func
            button.grid(column=col, row=row, padx=10)
            self.buttons.append(button)


def press(num):
    global expression

    if num not in (",", ".") and expression == "0":  # deletes first 0 (so we don't have something like 06, just 6)
        expression = ""
    if isinstance(num, str):  #checks if num is a string
        num = num.lower()  #lowers the first digit
        for key, value in window.operations.items():  #searches for function
            if key == num:
                resultFunction = window.operations[num]

                lastDigit = expression[-1]
                isNumber = lastDigit.isnumeric()
                if (not isNumber ) and lastDigit not in ("(", ")", "."):
                    print(lastDigit)
                    expression = expression[:-1]

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


def divide():  #divides the number
    global expression

    expression = expression + "/"
    textBox.set(expression)


def negation():  #negation of number
    global expression

    if expression != "0" and len(expression) >= 1:
        if expression[0] == "-":
            expression = expression[1:]
        else:
            expression = "-" + expression
        textBox.set(expression)


def squareRoot():  #square root
    global expression

    match = re.search(r'((\d+)+(\D*))$', expression)  # r-raw string

    if match:
        lastNumber = match.group()
        restOfExpression = expression[:match.start(1)]

        expression = f"{restOfExpression}√({lastNumber})"

        textBox.set(expression)


def floatNum():
    global expression
    expression = expression + "."
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

    while expression.count("(") > expression.count(")"):  #to make sure brackets are closed
        expression += ")"
    try:
        expression = expression.replace("√", "sqrt")  #checking for sqrt

        # Pozwalamy eval używać oprócz wbudowanych jeszcze sqrt
        result = eval(expression, {'sqrt': sqrt})
        print(result)

        textBox.set(str(result))  # We show result
        expression = str(result)  # Saving the result

    except TypeError as e:
        textBox.set("Error")  # Obsługa błędów (np. dzielenie przez 0)
        print(e)
        expression = ""

    except SyntaxError as syn:
        expression = expression[:-1]
        textBox.set(expression)
        print("You can't do it")


window = Window()

textBox = StringVar()  #text were value of result is displayed
textBox.set("0")  #default value

#field where result is displayed
expressionField = CTkEntry(window, textvariable=textBox, font=('arial', 18, 'bold'))
expressionField.grid(columnspan=5, column=0, row=0, ipadx=90, ipady=10)

print("ok")

#starts the program
window.mainloop()
