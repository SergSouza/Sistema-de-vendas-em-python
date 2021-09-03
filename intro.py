from tkinter import font, ttk
from tkinter import *
from PIL import ImageTk, Image



class splash:
    def __init__(self):
        self.splashMainW = Tk()
        self.splashMainW.title ('Sistema de vendas em python tkinter')

        Width = 1000
        height = 680

        self.splashMainW.config(bg='#BF8C4E')
        tela_largura = self.splashMainW.winfo_screenwidth()
        tela_altura = self.splashMainW.winfo_screenheight()

        x = (tela_largura / 2) - (Width / 2)
        y = (tela_altura / 2) - (height / 2)

        self.splashMainW.geometry("%dx%d+%d+%d" %(Width,height,x,y))
        self.splashMainW.resizable(0,0)
        
        #trazendo nossa imagem
        path = 'imagens/user.png'
        img = ImageTk.PhotoImage(Image.open(path))

        # splashMainW == formulario
        # main == label
        # fotoFlame == imagens


        #trabalhando nosso label
        main = LabelFrame(self.splashMainW,width=890,height=560,bg='#8C8177', relief='sunken')
        main.place(x=55,y=70)

        #trabalhando nossa imagen
        FotoFrame = LabelFrame(main,width=420,height=444,bg='#8C8177',bd=0, relief='raised')
        foto =  Label(FotoFrame,image=img)
        foto.place (x=6,y=6)
        FotoFrame.place(x=10,y=100)

        #Label(main, text="", font="",bg="").place(x="",y="")
        Label(main,text="Sistema de vendas em python sqlite",font="arial 28 bold",bg="#8C8177").place(x="45",y="10")               
        Label(main,text="Faculdade FATEPI",font="arial 32 bold",bg="#8C8177").place(x="450",y="160")
        Label(main,text="CURSO: python (Prof= Aratã)",font="arial 16 bold",bg="#8C8177").place(x="445",y="260")
        Label(main,text="DESENVOLVEDOR: Sergio Souza",font="arial 16 bold",bg="#8C8177").place(x="445",y="310")
        Label(main,text="EMAIL: sergio.escureto@gmail.com",font="arial 16 bold",bg="#8C8177").place(x="445",y="360")
        Label(main,text="TELEFONE: (99) 984717748",font="arial 16 bold",bg="#8C8177").place(x="445",y="410")

        self.Continuar = Button(self.splashMainW,width=20,text="Continuar",anchor="center",bg="green",fg="dimgray",font="roboto 14",foreground="white")
        self.Continuar.place(x=600,y=580)
        #aqui entra as mensg de boa vindas 

        self.splashMainW.mainloop()

      
