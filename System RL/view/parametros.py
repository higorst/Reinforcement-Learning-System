# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

from time import sleep

import constants.constants as constants
from view import Router
from view import popup as popup_

from view.code.aprendizado import configAR

def view(TelaInicial, dict_):  

    dict_config = {
        "experimento_titulo" : dict_["experimento_titulo"],
        "experimento_id" : dict_["experimento_id"],
        "alpha" : 0,
        "gamma" : 0,
        "epsilon" : 0,
        "algorithm" : 1,
        "monitor" : 1,
        "episodes" : 20,
        "episode" : 1,
        "started" : False,
        "matriz" : {},
    }

    def popup(s):
        popup_.run(s)

    def router(id, dict_config = None):
        Router.router(id, TelaInicial, dict_config)

    def validar():
        if (int(episodes.get()) >= 1 and
            float(alpha.get()) <= 1 and float(alpha.get()) >= 0 and
            float(gamma.get()) <= 1 and float(gamma.get()) >= 0 and
            float(epsilon.get()) <= 1 and float(epsilon.get()) >= 0 and
            str(var_algorithm.get()) != '' and
            str(var_matriz.get()) != '' and str(var_monitor.get()) != ''):

            if int(var_monitor.get()) == 1:
                dict_config["monitor"] = constants.btModoViewActive
            else:
                dict_config["monitor"] = constants.btModoViewInactive

            dict_config["alpha"] = alpha.get()
            dict_config["gamma"] = gamma.get()
            dict_config["epsilon"] = epsilon.get()
            if int(var_algorithm.get()) == 1:
                dict_config["algorithm"] = 'Q_Learning'
            else:
                dict_config["algorithm"] = 'Sarsa'
            dict_config["episodes"] = episodes.get()
            dict_config["matriz"] = var_matriz.get()

            # ------------------------------------------------------
            # Apaga conteúdo da view
            lista = TelaInicial.winfo_children()
            for l in lista:
                l.destroy()
            # ------------------------------------------------------
            # Logo
            img = Image.open(constants.addressAR)
            logo = ImageTk.PhotoImage(img)
            panel = Label(TelaInicial, image=logo, bg=constants.backgroundColor)
            panel.place(x=400, y=100, anchor=CENTER)
            # ------------------------------------------------------
            lb = Label(
                TelaInicial, 
                text="\n\n\nAguarde ...\n\n\nAplicando definições ...\n\n\nCriando Ensaio ...", 
                bg=constants.backgroundColor,
                fg="#757575"
            )
            lb.config(
                font=(
                    constants.fontPersonalizada, 
                    15
                )
            )
            lb.place(
                x=300, 
                y=300,
                anchor=W
            )
            # ------------------------------------------------------
            TelaInicial.update_idletasks()
            
            # Escrever alterações no arquivo
            if configAR.run(dict_config, 1):
                # ./configure && make
                if (configAR.run(dict_config, 2)):
                    # chamar próxima tela
                    sleep(1)
                    router(22, dict_config)
        else:
            msg = 'Parâmetros inválidos!'
            popup(msg)

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
    # Logo
    img = Image.open(constants.addressAR)
    logo = ImageTk.PhotoImage(img)
    panel = Label(TelaInicial, image=logo, bg=constants.backgroundColor)
    panel.place(x=400, y=100, anchor=CENTER)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Configurações do AR - INÍCIO
    # ------------------------------------------------------
    dist_x = 210
    # Episodes
    Label(
        TelaInicial, 
        text=constants.labelEpisodes,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=200, 
        anchor=W
    )
    episodes = Entry(TelaInicial)
    episodes.place(
        x=dist_x + 170, 
        y=200, 
        anchor=W
    )

    # Alpha
    Label(
        TelaInicial, 
        text=constants.labelAlpha,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=250, 
        anchor=W
    )
    alpha = Entry(TelaInicial)
    alpha.place(
        x=dist_x + 170, 
        y=250, 
        anchor=W
    )

    Label(
        TelaInicial, 
        text=constants.labelGamma,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=300, 
        anchor=W
    )
    gamma = Entry(TelaInicial)
    gamma.place(
        x=dist_x + 170, 
        y=300, 
        anchor=W
    )

    Label(
        TelaInicial, 
        text=constants.labelEpsilon,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=350, 
        anchor=W
    )
    epsilon = Entry(TelaInicial)
    epsilon.place(
        x=dist_x + 170, 
        y=350, 
        anchor=W
    )

    Label(
        TelaInicial, 
        text=constants.labelAlgorithm,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=400, 
        anchor=W
    )

    Label(
        TelaInicial, 
        text=constants.labelMatriz,
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=450, 
        anchor=W
    )

    Label(
        TelaInicial, 
        text="Monitor",
        bg=constants.backgroundColor
    ).place(
        x=dist_x + 10, 
        y=500, 
        anchor=W
    )

    # RADIO BUTTON ALGORITHM
    var_algorithm = IntVar()
    algorithm_1 = Radiobutton(
        TelaInicial, 
        text="Q_Learning", 
        variable=var_algorithm, 
        value=1,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    algorithm_1.place(
        x=dist_x + 170, 
        y=400, 
        anchor=W
    )

    algorithm_2 = Radiobutton(
        TelaInicial, 
        state=DISABLED,
        text="Sarsa",  
        variable=var_algorithm, 
        value=2,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    algorithm_2.place(
        x=dist_x + 290, 
        y=400, 
        anchor=W
    )

    # RADIO BUTTON MATRIZ
    var_matriz = IntVar()
    matriz_1 = Radiobutton(
        TelaInicial, 
        text="Atual", 
        variable=var_matriz, 
        value=1,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    matriz_1.place(
        x=dist_x + 170, 
        y=450, 
        anchor=W
    )

    matriz_2 = Radiobutton(
        TelaInicial, 
        text="Nova",  
        variable=var_matriz, 
        value=2,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    matriz_2.place(
        x=dist_x + 290, 
        y=450, 
        anchor=W
    )

    # RADIO BUTTON MONITOR
    var_monitor = IntVar()
    monitor_1 = Radiobutton(
        TelaInicial, 
        text="Ativado", 
        variable=var_monitor, 
        value=1,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    monitor_1.place(
        x=dist_x + 170, 
        y=500, 
        anchor=W
    )

    monitor_2 = Radiobutton(
        TelaInicial, 
        text="Desativado",  
        variable=var_monitor, 
        value=2,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    monitor_2.place(
        x=dist_x + 290, 
        y=500, 
        anchor=W
    )

    # ------------------------------------------------------
    #  INFO --
    # ------------------------------------------------------

    image = Image.open(constants.addressInfo)
    image = image.resize((constants.sizeIconInfo, constants.sizeIconInfo), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(image)

    # ------------------------------------------------------
    # Episodes
    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=constants.sizeIconInfo, 
        image=icon,
        command=lambda popup=popup: popup(constants.infoEpisodes),
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=dist_x + 150, 
        y=200, 
        anchor=W
    )
    # ------------------------------------------------------

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
        x=dist_x + 150, 
        y=250, 
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
        x=dist_x + 150, 
        y=300, 
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
        x=dist_x + 150, 
        y=350, 
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
        x=dist_x + 150, 
        y=400, 
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
        x=dist_x + 150, 
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
        command=lambda popup=popup: popup("Ativar ou não monitor para assistir as partidas!"),
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=dist_x + 150, 
        y=500, 
        anchor=W
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Configurações do AR - FIM
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=5, 
        text=constants.btTelaInicial, 
        command=lambda router=router: router(2),
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
    # Button Next
    # ------------------------------------------------------
    bt = Button(
        TelaInicial, 
        width=5, 
        text='Next', 
        command=lambda validar=validar: validar(),
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=725, 
        y=595, 
        anchor=SE
    )
    # ------------------------------------------------------

    TelaInicial.mainloop()
