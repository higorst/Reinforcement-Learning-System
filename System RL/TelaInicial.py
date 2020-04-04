#coding: utf-8
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
from view import Router

def TelaInicial(TelaInicial):

    # ------------------------------------------------------
    def router(id):        
        Router.router(id, TelaInicial)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Definições da view
    if (TelaInicial == None):
        TelaInicial = Tk()
        TelaInicial.geometry(constants.viewSize)
        TelaInicial.resizable(0,0)
    TelaInicial.title(constants.titleTelaInicial)
    TelaInicial.configure(
        background=constants.backgroundColor
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    lb = Label(
        TelaInicial, 
        text=constants.titleHome, 
        bg=constants.backgroundColor,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaIn
        )
    )
    lb.place(
        x=410, 
        y=20,
        anchor=N
    )
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
    bt = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial01, 
        command=lambda router=router: router(1), 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
    )    
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=400, 
        y=300, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial02, 
        command=lambda router=router: router(2),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=400, 
        y=350, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial03, 
        command=lambda router=router: router(3),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=400, 
        y=400, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial04, 
        command=lambda router=router: router(4),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=400, 
        y=450, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial05, 
        command=lambda router=router: router(5),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=400, 
        y=500, 
        anchor=CENTER
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
        x=795, 
        y=595, 
        anchor=SE
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    lb = Label(
        TelaInicial, 
        text=constants.titleCopyright, 
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
        x=10, 
        y=595, 
        anchor=SW
    )
    # ------------------------------------------------------
    router(2)

    TelaInicial.mainloop()

if __name__ == '__main__':
    view = TelaInicial(None)