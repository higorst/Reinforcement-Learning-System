# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
import TelaInicial as telaInicial
from view import Router as router

def view(TelaInicial):	

    def Sair():
        TelaInicial.destroy()
        TelaInicial.quit()

    def Menu():
        id = 0
        router.router(id, TelaInicial)

    TelaInicial.title(
    	constants.titleTela05
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