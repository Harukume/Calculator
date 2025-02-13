from tkinter import Tk, Button

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
        super().__init__() # inheritance from Tk

        self.title("Calculator")
        self.button = Button(text="Click me")


#creates object and starts the program
window = Window()
window.mainloop()