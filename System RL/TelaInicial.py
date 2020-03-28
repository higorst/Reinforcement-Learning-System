#coding: utf-8
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
from view import aprendizado

def TelaInicial():

    # ------------------------------------------------------
    def Sair():
        TelaInicial.destroy()
        TelaInicial.quit()
    # ------------------------------------------------------

    # ------------------------------------------------------
    def rodarAprendizado():
        # TelaInicial.destroy()
        aprendizado.viewAprendizado(TelaInicial)
        pass
    # ------------------------------------------------------

    # ------------------------------------------------------
    def getResults():
        # TelaInicial.destroy()
        # Consulta.TelaConsulta()
        pass
    # ------------------------------------------------------

    # ------------------------------------------------------
    def about():
        pass
    # ------------------------------------------------------

    # ------------------------------------------------------
    TelaInicial = Tk()
    TelaInicial.geometry(constants.viewSize)
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
    btCadastro = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial01, 
        command=rodarAprendizado, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
    )
    btCadastro.place(
        x=400, 
        y=300, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    btConsulta = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial02, 
        command=getResults, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btConsulta.place(
        x=400, 
        y=350, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    btEmitirNota = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial03, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btEmitirNota.place(
        x=400, 
        y=400, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    btImprimirAdesivo = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial04, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btImprimirAdesivo.place(
        x=400, 
        y=450, 
        anchor=CENTER
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    btDuplicata = Button(
        TelaInicial, 
        width=15, 
        text=constants.btTelaInicial05, 
        command=about, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btDuplicata.place(
        x=400, 
        y=500, 
        anchor=CENTER
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
    TelaInicial()

