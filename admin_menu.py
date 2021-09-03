import sqlite3
from tkinter import ttk
from tkinter import *


class Admin:
    def Admin_mainMenu(self,a,b):
        self.mainframe = LabelFrame(self.MainW,width=1200,height=145,bg="#BFBBB4")
        self.mainframe.place(x=100, y=100)

        #crindo nossos button de navergação e colocando nossos icon

        # Perfil
        imgP = PhotoImage(file="imagens/perfil.png")
        imgP = imgP.subsample(a,b)
        self.conta = Button(self.mainframe,font="arial 10 bold ", image=imgP,text = "Perfil",bd=3,command=TOP)
        self.conta.place(x=665, y=27)
        self.conta.image=imgP

        # Sair
        imgS = PhotoImage(file="imagens/sair.png")
        imgS = imgS.subsample(a,b)
        self.sair = Button(self.mainframe,text="sair",font="arial 11 bold ",image=imgS,bd=3,command=TOP)
        self.sair.place(x=1050, y=27)
        self.sair.image=imgS

        # trocar usuario
        imgT = PhotoImage(file="imagens/trocarusuario.png")
        imgT= imgT.subsample(a,b)
        self.trocarUsuario = Button(self.mainframe,text="Trocar Usuario",font="arial 11 bold ",image=imgT,bd=3,command=TOP)
        self.trocarUsuario.place(x=855, y=27)
        self.trocarUsuario.image=imgT
        
        # items
        imgI = PhotoImage(file="imagens/items.png")
        imgI= imgI.subsample(a,b)
        self.items = Button(self.mainframe,text="Items",font="arial 11 bold ",image=imgI,bd=3,command=TOP,bg="#0C2E59")
        self.items.place(x=47, y=27)
        self.items.image=imgI


        #inventario
        imgIN = PhotoImage(file="imagens/inventario.png")
        imgIN= imgIN.subsample(a,b)
        self.Inventario = Button(self.mainframe,text="Inventario",font="arial 11 bold ",image=imgIN,bd=3,command=TOP,bg="#0C2E59")
        self.Inventario.place(x=255, y=27)
        self.Inventario.image=imgIN

        


        # venda
        imgV = PhotoImage(file="imagens/vendas.png")
        imgV= imgV.subsample(a,b)
        self.Vendas = Button(self.mainframe,text = "Vendas",font="arial 11 bold ",image=imgV,bd=3,command=TOP,bg="#0C2E59")
        self.Vendas.place(x=450, y=27)
        self.Vendas.image=imgV


        self.formframe = Frame(self.MainW,width=500,height=550,bg="#F2EBDC")
        self.formframe.place(x=100,y=315)