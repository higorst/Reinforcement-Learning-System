# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
import TelaInicial as telaInicial

def viewAprendizado(TelaInicial):	

    def limparFrame():
        lista = TelaInicial.winfo_children()
        for l in lista:
            l.destroy()

    def Sair():
        TelaInicial.destroy()
        TelaInicial.quit()

    def Menu():
        TelaInicial.destroy()
        telaInicial.TelaInicial()

    limparFrame()
    TelaInicial.title(
    	constants.titleTelaAprendizado
    )
    TelaInicial.configure(
    	background=constants.backgroundColor
    )

    # ------------------------------------------------------
    btMenu = Button(
        TelaInicial, 
        width=5, 
        text=constants.btTelaInicial, 
        command=Menu,
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btMenu.place(
        x=795, 
        y=595, 
        anchor=SE
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    btSair = Button(
        TelaInicial, 
        width=5, 
        text=constants.btExit, 
        command=Sair,
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btSair.place(
        x=10, 
        y=595, 
        anchor=SW
    )
    # ------------------------------------------------------