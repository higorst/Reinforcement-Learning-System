# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants
from view import Router

# ------------------------------------------------------
# requisitos:
# ------------------------------------------------------

# ------------------------------------------------------
# Algumas configurações:
#       - Parâmetros: taxa de aprendizado, fator de desconto e e-greedy.
#       - Algoritmo de AR.
#       - Número de episódios.
#       - Matriz de aprendizado: utilizar uma zerada ou outra com já aprendizado acumulado.
# Resultados:
#       - Gráficos: saldo de gols, gols feitos ou gols sofridos.
#       - Ou de forma mais simples: mostras os valores em caixas de texto (média dos intervalos).
# ------------------------------------------------------

def view(TelaInicial):  

    dict_config = {
        "alpha" : 0,
        "gamma" : 0,
        "epsilon" : 0,
        "algorithm" : '',
        "episodes" : 0,
        "matriz" : {},
    }

    # alpha => entrado de número - garantir float 0-1
    # gamma => entrado de número - garantir float 0-1
    # epsilon => entrado de número - garantir float 0-1

    def closePopup(popupRoot):
        # Finaliza popup
        popupRoot.destroy()
        popupRoot.quit()

    def popup(s):
        popupRoot = Tk()
        popupRoot.title('INFO')
        popupRoot.configure(
            background=constants.backgroundColor
        )
        popupRoot.after(3000, lambda getTeam=closePopup: closePopup(popupRoot))
        Label(
            popupRoot, 
            text='',
            bg=constants.backgroundColor
        ).pack()
        Label(
            popupRoot, 
            text=s,
            bg=constants.backgroundColor
        ).pack()
        popupRoot.geometry('400x50+500+300')
        popupRoot.mainloop()

    def router(id):
        Router.router(id, TelaInicial)

    def render():
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
        # Congiurações do AR - INÍCIO
        # ------------------------------------------------------
        dist_x = 250
        # Alpha
        Label(
            TelaInicial, 
            text="Alpha",
            bg=constants.backgroundColor
        ).place(
            x=dist_x, 
            y=300, 
            anchor=W
        )
        alpha = Entry(TelaInicial)
        alpha.place(
            x=dist_x + 100, 
            y=300, 
            anchor=W
        )

        Label(
            TelaInicial, 
            text="Gamma",
            bg=constants.backgroundColor
        ).place(
            x=dist_x, 
            y=350, 
            anchor=W
        )
        gamma = Entry(TelaInicial)
        gamma.place(
            x=dist_x + 100, 
            y=350, 
            anchor=W
        )

        Label(
            TelaInicial, 
            text="Epsilon",
            bg=constants.backgroundColor
        ).place(
            x=dist_x, 
            y=400, 
            anchor=W
        )
        epsilon = Entry(TelaInicial)
        epsilon.place(
            x=dist_x + 100, 
            y=400, 
            anchor=W
        )

        Label(
            TelaInicial, 
            text="Algorithm",
            bg=constants.backgroundColor
        ).place(
            x=dist_x, 
            y=450, 
            anchor=W
        )
        algorithm = Entry(TelaInicial)
        algorithm.place(
            x=dist_x + 100, 
            y=450, 
            anchor=W
        )

        Label(
            TelaInicial, 
            text="Matriz",
            bg=constants.backgroundColor
        ).place(
            x=dist_x, 
            y=500, 
            anchor=W
        )
        matriz = Entry(TelaInicial)
        matriz.place(
            x=dist_x + 100, 
            y=500, 
            anchor=W
        )

        # icon = PhotoImage(file = constants.addressInfo)

        image = Image.open(constants.addressInfo)
        image = image.resize((constants.sizeIconInfo, constants.sizeIconInfo), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(image)

        # ------------------------------------------------------
        # Alpha
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.sizeIconInfo, 
            image=icon,
            command=lambda popup=popup: popup(constants.infoAlpha),
            bg=constants.backgroundColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        bt.config(highlightbackground=constants.buttonHighLight)
        bt.place(
            x=dist_x + 80, 
            y=300, 
            anchor=W
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Gamma
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.sizeIconInfo, 
            image=icon,
            command=lambda popup=popup: popup(constants.infoGamma),
            bg=constants.backgroundColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        bt.config(highlightbackground=constants.buttonHighLight)
        bt.place(
            x=dist_x + 80, 
            y=350, 
            anchor=W
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Epsilon
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.sizeIconInfo, 
            image=icon,
            command=lambda popup=popup: popup(constants.infoEpsilon),
            bg=constants.backgroundColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        bt.config(highlightbackground=constants.buttonHighLight)
        bt.place(
            x=dist_x + 80, 
            y=400, 
            anchor=W
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Algorithm
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.sizeIconInfo, 
            image=icon,
            command=lambda popup=popup: popup(constants.infoAlgorithm),
            bg=constants.backgroundColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        bt.config(highlightbackground=constants.buttonHighLight)
        bt.place(
            x=dist_x + 80, 
            y=450, 
            anchor=W
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Matriz
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.sizeIconInfo, 
            image=icon,
            command=lambda popup=popup: popup(constants.infoMatriz),
            bg=constants.backgroundColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        bt.config(highlightbackground=constants.buttonHighLight)
        bt.place(
            x=dist_x + 80, 
            y=500, 
            anchor=W
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Congiurações do AR - FIM
        # ------------------------------------------------------

        # ------------------------------------------------------
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

    render()