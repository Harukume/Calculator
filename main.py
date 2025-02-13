from tkinter import Tk, Button, StringVar, Entry
from functools import partial

"""
    Main idea: make fancy calculator
    Do it in object oriented style

    Basic operations: +, -, *, /, sqrt(), % (percentage maybe)

    GUI for calculator (Tkinter)
    
    If free time:
        Make custom pixel(?) graphics
        
    How works:
    Take input from buttons (0-9), Store that data, do calculations, do until user quits and print final answer on CLI
"""
expression = ""  #global variable for holding result


class Window(Tk):
    """
    Settings of main window like layout of buttons, functions
    """

    def __init__(self):
        super().__init__()  # inheritance from Tk

        self.title("Calculator")
        self.configure(background="light green")
        self.geometry("300x300")

        self.buttons = []  #list for buttons

        buttonValues = [
            (1, 0, 1), (2, 1, 1), (3, 2, 1), ('Clear', 3, 1),
            (4, 0, 2), (5, 1, 2), (6, 2, 2),
            (7, 0, 3), (8, 1, 3), (9, 2, 3),
            (0, 1, 4),
        ]
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)
        for row in range(5):
            self.grid_rowconfigure(row, weight=1)

        for num, col, row in buttonValues:
            button = Button(self, text=str(num), bg="green", width=10, height=2,
                            command=partial(press,num))  #partial remembers to value to func
            button.grid(column=col, row=row, padx =1, pady =1)
            self.buttons.append(button)


def press(num):
    global expression

    if isinstance(num, str): #checks if num is a string
        clear()
    else:
        expression = expression + str(num)
        textBox.set(expression)
        print(expression)


def clear(): #clears the display
    global expression
    expression = "0"
    textBox.set(expression)


window = Window()

textBox = StringVar() #display the result
textBox.set("0")
expressionField = Entry(window, textvariable=textBox, font = ('arial', 18, 'bold'))
expressionField.grid(columnspan=4, column=0, row=0, ipadx=90, ipady=10)

#creates object and starts the program
print("ok")

window.mainloop()
