# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants

from view import Router
from view import popup as popup_
from view.code import home
from view.code import getPlacar
from view.code import getPlacar as placar

import info as Info

from time import sleep 
import os, glob            
from pathlib import Path

def view(TelaInicial, dict_config):	

    def popup(s):
        popup_.run(s)

    def router(id):
        Router.router(id, TelaInicial)
        pass

    popup(str(dict_config["episodes"]))

    # ------------------------------------------------------
    # Button Voltar
    # ------------------------------------------------------
    btMenu = Button(
        TelaInicial, 
        width=5, 
        text=constants.btTelaInicial, 
        command=lambda router=router: router(0),
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
    # Button Sair
    # ------------------------------------------------------
    btSair = Button(
        TelaInicial, 
        width=5, 
        text=constants.btExit, 
        command=lambda router=router: router(999),
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

    TelaInicial.mainloop()

