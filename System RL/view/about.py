# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants
from view import Router

import webbrowser

def view(TelaInicial):  

    def router(id):
        Router.router(id, TelaInicial)

    def callback(url):
        webbrowser.open_new(url)

    # ------------------------------------------------------
    # Definições da view
    TelaInicial.title(
        constants.titleTela01
    )
    TelaInicial.configure(
        background=constants.backgroundColor
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Informações da Equipe - START
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Logo UFRBots
    width = 100
    height = 132
    img = Image.open(constants.addressLogo)
    img = img.resize((width,height), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(img)
    panel = Label(TelaInicial, image=logo, bg=constants.backgroundColor)
    panel.place(x=400, y=170, anchor=CENTER)
    # ------------------------------------------------------

    # ------------------------------------------------------
    x_ = 400
    lb = Label(
        TelaInicial, 
        text='UFRBots - Equipe de Futebol de Robôs da UFRB\n' + 
             'UFRB - Universidade Federal do Recôncavo da Bahia\n' + 
             '\n' +
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             '\n' + 
             constants.titleHome + 
             '\nVersão 1.0\n\n' + 
             '\n', 
        bg=constants.backgroundColor,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeCopyright
        )
    )
    lb.place(
        x=x_, 
        y=380,
        anchor=CENTER
    )
    # ------------------------------------------------------
    link1 = Label(TelaInicial, text="Coordenação: Prof. André Luiz Carvalho Ottoni\nLattes: http://lattes.cnpq.br/2003401420560517", fg="black", bg=constants.backgroundColor, cursor="hand2")
    link1.place(
        x=x_, 
        y=333,
        anchor=CENTER
    )
    link1.bind("<Button-1>", lambda e: callback("http://lattes.cnpq.br/2003401420560517"))

    link2 = Label(TelaInicial, text="Site da equipe: ufrbots.github.io", fg="black", bg=constants.backgroundColor, cursor="hand2")
    link2.place(
        x=x_, 
        y=383,
        anchor=CENTER
    )
    link2.bind("<Button-1>", lambda e: callback("https://ufrbots.github.io/"))

    link2 = Label(TelaInicial, text="Desenvolvimento: Higor Santos de Jesus\nLattes: http://lattes.cnpq.br/3025535097086755", fg="black", bg=constants.backgroundColor, cursor="hand2")
    link2.place(
        x=x_, 
        y=486,
        anchor=CENTER
    )
    link2.bind("<Button-1>", lambda e: callback("http://lattes.cnpq.br/3025535097086755"))

    # ------------------------------------------------------
    # Informações da Equipe - END
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Informações do desenvolvimento - START
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Informações do desenvolvimento - END
    # ------------------------------------------------------

    # ------------------------------------------------------
    icon = PhotoImage(file = constants.addressHome)
    bt = Button(
        TelaInicial, 
        width=5, 
        text=constants.btTelaInicial,
        command=lambda router=router: router(0),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=795, 
        y=595, 
        anchor=SE
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=5, 
        text=constants.btExit, 
        command=lambda router=router: router(999),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=10, 
        y=595, 
        anchor=SW
    )
    # ------------------------------------------------------

    TelaInicial.mainloop()