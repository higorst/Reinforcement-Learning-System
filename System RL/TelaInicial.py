#coding: utf-8
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import os
import subprocess

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
        input_ = "who"
        var = subprocess.getoutput(input_)
        var = var.split()
        user_name = var[0]
        # -----------------------------------------
        # Configurar .desktop
        # -----------------------------------------
        addressFileDesktop = "/home/" + user_name + "/.System RL/System RL.desktop"
        path = addressFileDesktop
        file_ = open(path, 'r')

        new = ''
        for line in file_:
            l = line
            if "Exec=" in l:
                l = "Exec=" + str(constants.commandExec) + "\n"
            elif "Icon=" in l:
                l = "Icon=" + str(constants.commandIcon) + "\n"
            new += l

        file_.close()
        
        f_ = open(path, 'w')
        f_.write(new)
        f_.close()

        # Mover file desktop
        input_ = "cd && cp -r /home/" + user_name + "/.System\ RL/System\ RL.desktop /usr/share/applications/"
        var = subprocess.getoutput(input_)
        # input_ = "cd && cp -r /usr/share/applications/System\ RL.desktop /home/" + user_name + "/Desktop/"
        # var = subprocess.getoutput(input_)

        # construir tela
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

    TelaInicial.mainloop()

if __name__ == '__main__':
    view = TelaInicial(None)