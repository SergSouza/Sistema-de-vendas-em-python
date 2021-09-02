from tkinter import ttk
from tkinter import *
from intro import splash
from usuario import Login

class Main_Principal(splash,Login):
    def __init__(self):
        global b 
        if b == 0:
            super().__init__()
            b==1
        Login.__init__(self)
        self.loginW.mainloop()

if __name__ == '__main__':
    b = 0 
    w = Main_Principal()