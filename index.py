from tkinter import ttk
from tkinter import *
from intro import splash
from usuario import Login
from admin_menu import Admin

class Main_Principal(splash,Login,Admin):
    def __init__(self):
        global b 
        if b == 0:
            super().__init__()
            b==1
        Login.__init__(self)
        self.loginW.mainloop()
        self.MainW=Toplevel(bg='#BF8C4E')
        Width = 1350
        height = 720

        tela_largura = self.MainW.winfo_screenwidth()
        tela_altura = self.MainW.winfo_screenheight()

        x = (tela_largura / 2) - (Width / 2)
        y = (tela_altura / 2) - (height / 2)

        self.MainW.geometry("%dx%d+%d+%d" %(Width,height,x,y))
        self.MainW.title ('Sistema de vendas em python tkinter')
        self.MainW.resizable(0,0)

        self.getdetalhe()

    #pegando dados do banco de dados se for admin  ou usuario
    def getdetalhe(self):
        self.amontarMain()
    
    #mandando pra tela administrador
    def amontarMain(self):
        self.Admin_mainMenu(8,8)



if __name__ == '__main__':
    b = 0 
    w = Main_Principal()
    w.MainW.mainloop()