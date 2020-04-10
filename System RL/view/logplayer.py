# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

from view import popup as popup_

import os
import subprocess

import constants.constants as constants
from view import Router
from view.code import logs

def view(TelaInicial):  

    itens_name, itens_show = logs.run()

    def router(id):
        Router.router(id, TelaInicial)

    def popup(s):
        popup_.run(s, 2000)

    def start():
        line = listbox.curselection()
        if line == ():
            popup(constants.msgToSelectLogplayer)
        else:
            # iniciar rcsslogplayer
            input_ = 'cd && rcsslogplayer /home/ufrbots/logAR/' + itens_name[int(line[0])]
            var = subprocess.getoutput(input_)

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
    lb = Label(
        TelaInicial, 
        text=constants.titleLogplayer, 
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
    lb = Label(
        TelaInicial, 
        text=constants.infoLogplayer, 
        bg=constants.backgroundColor,
        fg="#757575"
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeCopyright
        )
    )
    lb.place(
        x=250, 
        y=100,
        anchor=W
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    # listbox partida
    # ------------------------------------------------------
    listbox = Listbox(
        TelaInicial,
        width=72,
        height=18,
        font=constants.fontPersonalizadaList,
        fg=constants.listboxFG,
        bg=constants.listboxBG,
        bd=0,
        selectmode=SINGLE
    )
    listbox.configure(justify=LEFT)
    listbox.place(
        x=40, 
        y=370, 
        anchor=W
    )
    for item in itens_show:
        listbox.insert(END, item)
    # ------------------------------------------------------

    y_ = 160
    # ------------------------------------------------------
    # date
    width = 30
    height = width
    img_1 = Image.open(constants.addressDate)
    img_1 = img_1.resize((width,height), Image.ANTIALIAS)
    logo_1 = ImageTk.PhotoImage(img_1)
    panel_1 = Label(TelaInicial, image=logo_1, bg=constants.backgroundColor)
    panel_1.place(x=125, y=y_, anchor=CENTER)
    # ------------------------------------------------------
    # ------------------------------------------------------
    # hour
    img_2 = Image.open(constants.addressHour)
    img_2 = img_2.resize((width,height), Image.ANTIALIAS)
    logo_2 = ImageTk.PhotoImage(img_2)
    panel_2 = Label(TelaInicial, image=logo_2, bg=constants.backgroundColor)
    panel_2.place(x=68 + 295, y=y_, anchor=CENTER)
    # ------------------------------------------------------
    # ------------------------------------------------------
    # scoreboard
    img_3 = Image.open(constants.addressScoreboard)
    img_3 = img_3.resize((width,height), Image.ANTIALIAS)
    logo_3 = ImageTk.PhotoImage(img_3)
    panel_3 = Label(TelaInicial, image=logo_3, bg=constants.backgroundColor)
    panel_3.place(x=68 + 565, y=y_, anchor=CENTER)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Button Start
    # ------------------------------------------------------
    btMenu = Button(
        TelaInicial, 
        width=76, 
        text="Assistir", 
        command=start,
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