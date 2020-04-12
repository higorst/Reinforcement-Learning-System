# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import threading
from view import popup as popup_

import constants.constants as constants
from view import Router
from view.code import show_movie as sm

def view(TelaInicial):  

    def router(id):
        Router.router(id, TelaInicial)

    def msg():
        msg = 'Selecione uma opção!'
        popup_.run(msg, 2000)

    def show():
        c = True
        if int(var_op.get()) == 1:
            name = constants.addressMovie01
            t = constants.addressMovie01Time
        elif int(var_op.get()) == 2:
            name = constants.addressMovie02
            t = constants.addressMovie02Time
        elif int(var_op.get()) == 3:
            name = constants.addressMovie03
            t = constants.addressMovie03Time
        else:
            c = False
            threading.Thread(target=msg).start()
        if c:
            sm.run(name, t)

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

    # change directory
    img = Image.open(constants.addressPlay)
    img = img.resize((100,100), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(img)
    bt = Button(
        TelaInicial, 
        width=100, 
        image=icon, 
        command=show,
        bg=constants.activeButtonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColorInfo
    )
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=500, 
        y=250, 
        anchor=CENTER
    )

    # ------------------------------------------------------

    # RADIO BUTTON
    dist_x = 150
    var_op = IntVar()
    op_1 = Radiobutton(
        TelaInicial, 
        text=constants.btTelaInicial01, 
        variable=var_op, 
        value=1,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    op_1.place(
        x=dist_x, 
        y=200, 
        anchor=W
    )

    op_2 = Radiobutton(
        TelaInicial, 
        text=constants.btTelaInicial02,  
        variable=var_op, 
        value=2,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    op_2.place(
        x=dist_x, 
        y=250, 
        anchor=W
    )

    op_3 = Radiobutton(
        TelaInicial, 
        text=constants.btTelaInicial03,  
        variable=var_op, 
        value=3,
        bg=constants.backgroundColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
        highlightbackground=constants.backgroundColor
    )
    op_3.place(
        x=dist_x, 
        y=300, 
        anchor=W
    )

    # op_4 = Radiobutton(
    #     TelaInicial, 
    #     text=constants.btTelaInicial04,  
    #     variable=var_op, 
    #     value=4,
    #     bg=constants.backgroundColor, 
    #     fg=constants.letterColor,
    #     activebackground=constants.activeButtonColor,
    #     highlightbackground=constants.backgroundColor
    # )
    # op_4.place(
    #     x=dist_x, 
    #     y=450, 
    #     anchor=W
    # )

    # op_5 = Radiobutton(
    #     TelaInicial, 
    #     text=constants.btTelaInicial05,  
    #     variable=var_op, 
    #     value=5,
    #     bg=constants.backgroundColor, 
    #     fg=constants.letterColor,
    #     activebackground=constants.activeButtonColor,
    #     highlightbackground=constants.backgroundColor
    # )
    # op_5.place(
    #     x=dist_x, 
    #     y=500, 
    #     anchor=W
    # )

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