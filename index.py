from tkinter import ttk
from tkinter import *
from intro import splash

class Main_Principal(splash):
    def __init__(self):
        global b 
        if b == 0:
            super().__init__()

if __name__ == '__main__':
    b = 0 
    w = Main_Principal()