from tkinter import Tk, Button, StringVar, Entry

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


class Window(Tk):
    """
    Settings of main window like layout of buttons, functions
    """

    def __init__(self):
        super().__init__()  # inheritance from Tk

        self.title("Calculator")
        self.configure(background="light green")
        self.geometry("300x300")

        self.button = Button(text="Click me").grid(column=2, row=1)


class Equation(StringVar):
    def __init__(self):
        super().__init__()


window = Window()

textBox = Equation()
expressionField = Entry(window, textvariable=textBox)
expressionField.grid(columnspan=3, row=0, ipadx=100)

#creates object and starts the program
print("ok")

window.mainloop()
