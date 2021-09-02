import sqlite3

from tkinter import font, ttk
from tkinter import *
from tkinter import messagebox

class Login :
    #criando nossa tela de login
    def __init__(self):
        #criando nossa tela de login
        self.loginW = Tk()
        self.loginW.title("login:")

        #passando o tamanho da nossa tela 
        width = 500
        height = 600


        #configurando nossa tela e posicionamento 
        self.loginW.config(bg="darkblue")
        tela_largura = self.loginW.winfo_screenwidth()
        tela_altura = self.loginW.winfo_screenheight()
        x = (tela_largura / 2 ) - (width / 2 )
        y = (tela_altura / 2 ) - (height / 2 )
        self.loginW.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.loginW.resizable(0,0)
        #atibuindo um valor pro nosso inputs
        self.username = StringVar(value="Nome Usuario")
        self.senha = StringVar(value="Password usuario")
        
        #chamando nossas funcao obj
        self.objetos_login()

    #criando nossos campo de interaçao na nossa tela de login
    def objetos_login(self):
        #criando uma campo onde vamos colocar nossos imputs
        self.longiFrame = LabelFrame(self.loginW,bg="#4267b2",height=400,width=300)
        self.longiFrame.place(x=103,y=95)
        # colocando nosso title
        self.toplabel = Label(self.longiFrame,fg="white", bg="#4267b2", anchor="center",text="Login",font="arial 35 bold")
        self.toplabel.place(x=75,y=25)
        #nossos campos
        self.us = ttk.Entry(self.longiFrame, textvariable=self.username, width=20,font="Roboto 14")
        self.us.place(x=35,y=145,height=40)
        self.pa = ttk.Entry(self.longiFrame, textvariable=self.senha, width=20,font="Roboto 14")
        self.pa.place(x=35,y=185,height=40)


        # criando um evento click em nosso campos
        self.us.bind('<Button-1>',self.onclick)
        self.pa.bind('<Button-1>',self.onclick1)

        #criando nosso botão de entrar
        self.signin = Button(self.longiFrame,width=10,text="Login",anchor="center",bg="darkgreen",fg="dimgray",font="roboto 14",foreground="white")
        self.signin.place(x=35,y=290)


    # funcoes q limpas nossos campos inputs ao clicar neles
    def onclick(self,event):
        self.us.delete(0,"end")

    def onclick1(self,event):
        self.pa.delete(0,"end")