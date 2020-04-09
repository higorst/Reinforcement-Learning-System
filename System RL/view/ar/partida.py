# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

import random

import constants.constants as constants

from view import Router
from view import popup as popup_
from view.code import home
from view.code import getPlacar
from view.code import getPlacar as placar

from view.code.aprendizado import start as start_

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

    def results():
        pass

    def verify():
        if not dict_config["episode"] > dict_config["episodes"] and dict_config["started"]:
            start()
        else:
            countMatch(1, 1)
            # ------------------------------------------------------
            # Button Start
            # ------------------------------------------------------
            btMenu = Button(
                TelaInicial, 
                width=76, 
                text="Resultados", 
                command=results,
                bg=constants.butonColorInfo, 
                fg=constants.letterColor,
                activebackground=constants.activeButtonColorInfo
            )
            btMenu.place(
                x=402, 
                y=579, 
                anchor=CENTER
            )
            # ------------------------------------------------------
            lb = Label(
                TelaInicial, 
                text="Aprendizado finalizado!", 
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

    def start():
        if not dict_config["started"]:
            dict_config["started"] = True
            # ------------------------------------------------------
            # Button Start
            # ------------------------------------------------------
            btMenu = Button(
                TelaInicial, 
                width=76, 
                text="Aguarde ..", 
                command=start,
                bg=constants.buttonStopColor, 
                fg=constants.letterColor,
                activebackground=constants.buttonStopColorActive
            )
            btMenu.place(
                x=402, 
                y=579, 
                anchor=CENTER
            )
        elif start_.run():
            countMatch(dict_config["episode"])
            progress_bar.set(int(dict_config["episode"]))

            ep = str(dict_config["episode"])
            r1 = str(random.randint(8, 16))
            r2 = str(random.randint(8, 16))

            while len(ep) <= 3:
                ep = ep + ' '

            while len(r1) <= 2:
                r1 = r1 + ' '

            while len(r2) <= 2:
                r2 = r2 + ' '

            str_ = " Partida - " + ep + " - AR  " + r1 + " X " + r2 + "  Reserva"
            # listbox.insert(END, "Partida " + str(dict_config["episode"]) + " -> AR  9  x  2  Reserva")
            
            listbox_1.insert(END, " Partida " + ep)
            listbox_2.insert(END, r1)
            listbox_3.insert(END, r2)

            listbox_1.see(listbox_1.size())
            listbox_2.see(listbox_2.size())
            listbox_3.see(listbox_3.size())

            # listbox.insert(END, str_)
            # listbox.see(listbox.size())

            dict_config["episode"] += 1

        TelaInicial.update_idletasks()
        TelaInicial.after_idle(verify())

    def countMatch(x, final = None):
        if final == None:
            desc = "Partida " + str(x) + " .."
        else:
            desc = "Episódios completos"
        # ------------------------------------------------------
        lbPartida = Label(
            TelaInicial, 
            text=desc, 
            bg=constants.backgroundColor,
            fg=constants.letterColor
        )
        lbPartida.config(
            font=(
                constants.fontPersonalizada, 
                constants.fontSizeTitleTelaIn
            )
        )
        lbPartida.place(
            x=410, 
            y=400,
            anchor=N
        )
        # lbPartida.after_idle(verify())
        # ------------------------------------------------------

    # AR x Reserva
    Label(
        TelaInicial, 
        text="AR    x    Res",
        bg=constants.backgroundColor,
        font='consolas',
    ).place(
        x=530, 
        y=90, 
        anchor=W
    )
    # Resultados
    Label(
        TelaInicial, 
        text="Resultados:",
        bg=constants.backgroundColor,
        font='consolas',
    ).place(
        x=395, 
        y=90, 
        anchor=W
    )
    # ------------------------------------------------------
    # listbox partida
    # ------------------------------------------------------
    listbox_1 = Listbox(
        TelaInicial,
        width=12,
        height=6,
        font='consolas',
        fg="#757575",
        bd=0,
    )
    listbox_1.configure(justify=RIGHT)
    listbox_1.place(
        x=380, 
        y=170, 
        anchor=W
    )
    # ------------------------------------------------------
    # ------------------------------------------------------
    # listbox result ar
    # ------------------------------------------------------
    listbox_2 = Listbox(
        TelaInicial,
        width=3,
        height=6,
        font='consolas',
        fg="#757575",
        bd=0,
    )
    listbox_2.configure(justify=RIGHT)
    listbox_2.place(
        x=530, 
        y=170, 
        anchor=W
    )
    # ------------------------------------------------------
    # ------------------------------------------------------
    # listbox result reserva
    # ------------------------------------------------------
    listbox_3 = Listbox(
        TelaInicial,
        width=3,
        height=6,
        font='consolas',
        fg="#757575",
        bd=0,
    )
    listbox_3.configure(justify=RIGHT)
    listbox_3.place(
        x=600, 
        y=170, 
        anchor=W
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    # percent 1
    width = 50
    height = 50
    img_1 = Image.open(constants.addressPercent_1)
    img_1 = img_1.resize((width,height), Image.ANTIALIAS)
    logo_1 = ImageTk.PhotoImage(img_1)
    panel_1 = Label(TelaInicial, image=logo_1, bg=constants.backgroundColor)
    panel_1.place(x=68, y=313, anchor=CENTER)
    # ------------------------------------------------------
    # ------------------------------------------------------
    # percent 2
    img_2 = Image.open(constants.addressPercent_2)
    img_2 = img_2.resize((width,height), Image.ANTIALIAS)
    logo_2 = ImageTk.PhotoImage(img_2)
    panel_2 = Label(TelaInicial, image=logo_2, bg=constants.backgroundColor)
    panel_2.place(x=68 + 328, y=313, anchor=CENTER)
    # ------------------------------------------------------
    # ------------------------------------------------------
    # percent 3
    img_3 = Image.open(constants.addressPercent_3)
    img_3 = img_3.resize((width,height), Image.ANTIALIAS)
    logo_3 = ImageTk.PhotoImage(img_3)
    panel_3 = Label(TelaInicial, image=logo_3, bg=constants.backgroundColor)
    panel_3.place(x=68 + 663, y=313, anchor=CENTER)
    # ------------------------------------------------------

    progress_bar = DoubleVar()

    s = ttk.Style()
    s.theme_use('clam')
    s.configure(
        "bar.Horizontal.TProgressbar",
        troughcolor=constants.backgroundColor, 
        bordercolor=constants.backgroundColor, 
        background=constants.butonColorInfo, 
        lightcolor=constants.butonColorInfo, 
        darkcolor=constants.activeButtonColorInfo
    )

    barra = ttk.Progressbar(
        TelaInicial, 
        style="bar.Horizontal.TProgressbar",
        length=700,
        variable=progress_bar, 
        orient="horizontal", 
        maximum=int(dict_config["episodes"]),
    )
    barra.place(
        x=400, 
        y=350,
        anchor=N
    )
    # ------------------------------------------------------
    lb = Label(
        TelaInicial, 
        text="Aprendendo ..", 
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

    dist_x = 100
    # Algorithm
    Label(
        TelaInicial, 
        text="Algoritmo",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=100, 
        anchor=W
    )
    # Alpha
    Label(
        TelaInicial, 
        text="Alpha",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=130, 
        anchor=W
    )
    # Gamma
    Label(
        TelaInicial, 
        text="Gamma",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=160, 
        anchor=W
    )
    # Epsilon
    Label(
        TelaInicial, 
        text="Epsilon",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=190, 
        anchor=W
    )
    # Episodes
    Label(
        TelaInicial, 
        text="Episódios",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=220, 
        anchor=W
    )

    dist_x = 170
    # Algorithm
    Label(
        TelaInicial, 
        text="->",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=100, 
        anchor=W
    )
    # Alpha
    Label(
        TelaInicial, 
        text="->",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=130, 
        anchor=W
    )
    # Gamma
    Label(
        TelaInicial, 
        text="->",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=160, 
        anchor=W
    )
    # Epsilon
    Label(
        TelaInicial, 
        text="->",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=190, 
        anchor=W
    )
    # Episodes
    Label(
        TelaInicial, 
        text="->",
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=220, 
        anchor=W
    )

    dist_x = 200
    # Algorithm
    Label(
        TelaInicial, 
        text=dict_config["algorithm"],
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=100, 
        anchor=W
    )
    # Alpha
    Label(
        TelaInicial, 
        text=dict_config["alpha"],
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=130, 
        anchor=W
    )
    # Gamma
    Label(
        TelaInicial, 
        text=dict_config["gamma"],
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=160, 
        anchor=W
    )
    # Epsilon
    Label(
        TelaInicial, 
        text=dict_config["epsilon"],
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=190, 
        anchor=W
    )
    # Episodes
    Label(
        TelaInicial, 
        text=dict_config["episodes"],
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=220, 
        anchor=W
    )

    # ------------------------------------------------------
    # Button Voltar
    # ------------------------------------------------------
    btMenu = Button(
        TelaInicial, 
        width=5, 
        text=constants.btMenu, 
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
    # ------------------------------------------------------
    # Button Start
    # ------------------------------------------------------
    btMenu = Button(
        TelaInicial, 
        width=76, 
        text=constants.btStart, 
        command=start,
        bg=constants.buttonColorConfig, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor
    )
    btMenu.place(
        x=402, 
        y=579, 
        anchor=CENTER
    )
    # lbPartida.after_idle(verify())

    # TelaInicial.after_idle(verify())
    TelaInicial.mainloop()
