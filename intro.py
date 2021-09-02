from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
        self.splashMainW = Tk()
        self.splashMainW.title ('Curso de venda em python tkinter')

        Width = 900
        height = 670

        self.splashMainW.config(bg='green')
        tela_largura = self.splashMainW.winfo_screenwidth()
        tela_altura = self.splashMainW.winfo_screenheight()

        x = (tela_largura / 2) - (Width / 2)
        y = (tela_altura / 2) - (height / 2)

        self.splashMainW.geometry("%dx%d+%d+%d" %(Width,height,x,y))
        self.splashMainW.resizable(0,0)
        
        #trazendo nossa imagem
        path = 'imagens/logo.png'
        img = ImageTk.PhotoImage(Image.open(path))

        # splashMainW == formulario
        # main == label
        # fotoFlame == imagens


        #trabalhando nosso label
        main = LabelFrame(self.splashMainW,width=700,height=570,bg='snow', relief='sunken')
        main.place(x=55,y=70)

        #trabalhando nossa imagen
        FotoFrame = LabelFrame(main,width=400,height=370,bg='snow', relief='raised')
        foto =  Label(FotoFrame,image=img)
        foto.place (x=6,y=6)
        FotoFrame.place(x=10,y=100)


        #aqui entra as mensg de boa vindas 

        self.splashMainW.mainloop()


