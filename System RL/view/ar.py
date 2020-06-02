# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import tkinter.font as tkFont
import tkinter.ttk as ttk

from time import sleep
import threading

import constants.constants as constants
from view import Router
from view import popup as popup_

from view.code.aprendizado import configAR
from view.bd import query

def view(TelaInicial):  

    experimentos_id, experimentos_titulo = query.getExperimentos()

    def dados():
        line = listbox.index(listbox.focus())
        if str(listbox.focus()) == "":
            popup("Selecione um experimento!")
        else:
            router(23, line)

    def update():
        global experimentos_id
        global experimentos_titulo

        # limpar listbox
        for r in listbox.get_children():
            listbox.delete(r)


        experimentos_id, experimentos_titulo = query.getExperimentos()
        i = 0
        for item in experimentos_titulo:
            listbox.insert('','end', item[0:], text=item[0:], values=(item[0:],))
            i += 1

    def cadastrar():
        render = False
        if (len(experimentos_id) == 0):
            render = True
        if str(titulo.get()) != '':
            query.cadastrarExperimento(str(titulo.get()))

            threading.Thread(target=lambda router=popup: popup("Experimento adicionado com sucesso!")).start()
            
            titulo.delete(0,END)
            titulo.insert(0,"")
        else:
            titulo.delete(0,END)
            titulo.insert(0,"")
            popup("Conteúdo inválido!")
        if render:
            router(2)
        else:
            # listbox.insert(titulo.get())
            update()

    def deletar():
        global experimentos_id
        global experimentos_titulo
        line = listbox.index(listbox.focus())
        if str(listbox.focus()) == "":
            popup("Selecione um experimento!")
        else:
            query.deletarExperimento(experimentos_id[int(line)])
            threading.Thread(target=lambda router=popup: popup("Experimento excluído!")).start()
            update()
            
        if (len(experimentos_id) == 0):
            router(2)

    def popup(s):
        popup_.run(s)

    def router(id, item = None):
        #  tela de parâmetros
        if ( id == 21 or id == 23 ):
            global experimentos_id
            global experimentos_titulo

            experimento_id = experimentos_id[int(item)]
            experimento_titulo = experimentos_titulo[int(item)]
            dict_config = {
                "experimento_titulo" : experimento_titulo,
                "experimento_id" : experimento_id,
            }

            Router.router(id, TelaInicial, dict_config)
        else:
            Router.router(id, TelaInicial)

    def next():
        line = listbox.index(listbox.focus())
        if str(listbox.focus()) == "":
            popup("Selecione um experimento para prosseguir ..")
        else:
            router(21, line)

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

    if (len(experimentos_id) > 0):
        container = ttk.Frame()
        container.place(x=40, y=240, width=721, height=300)
        titulos_listbox = ['Experimento']
        # create a treeview with dual scrollbars
        listbox = ttk.Treeview(columns=titulos_listbox, show="headings")
        vsb = ttk.Scrollbar(
            orient="vertical",
            command=listbox.yview
            )
        hsb = ttk.Scrollbar(
            orient="horizontal",
            command=listbox.xview
            )
        listbox.configure(
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
            )
        listbox.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for col in titulos_listbox:
            listbox.heading(col, text=col.title())
            # adjust the column's width to the header string
            listbox.column(col,
                width=tkFont.Font().measure(col.title()))
        update()

    # ------------------------------------------------------
    titulo = Entry(TelaInicial, width=70)
    titulo.place(
        x=40, 
        y=220, 
        anchor=W
    )
    bt = Button(
        TelaInicial, 
        width=15, 
        text="Cadastrar Aprendizado", 
        command=cadastrar, 
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColor,
    )    
    bt.config(highlightbackground=constants.buttonHighLight)
    bt.place(
        x=686, 
        y=220, 
        anchor=CENTER
    )
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

    if (len(experimentos_id) > 0):
        # ------------------------------------------------------
        # Button Delete
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=5, 
            text='Deletar', 
            command=deletar,
            bg="#ff0000", 
            fg=constants.letterColor,
            activebackground="#b30000"
        )
        bt.config(highlightbackground="#b30000")
        bt.place(
            x=585, 
            y=595, 
            anchor=SE
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Button Dados
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=5, 
            text='Dados', 
            command=dados,
            bg=constants.butonColorInfo, 
            fg=constants.letterColor,
            activebackground="#0b7dda"
        )
        bt.config(highlightbackground="#0b7dda")
        bt.place(
            x=655, 
            y=595, 
            anchor=SE
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Button Next
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=5, 
            text='Next', 
            command=next,
            bg="#33cc33", 
            fg=constants.letterColor,
            activebackground="#248f24"
        )
        bt.config(highlightbackground="#248f24")
        bt.place(
            x=725, 
            y=595, 
            anchor=SE
        )
        # ------------------------------------------------------
    else:
        # ------------------------------------------------------
        lb = Label(
            TelaInicial, 
            text="Cadastre um experimento para poder prosseguir ..", 
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
            y=400,
            anchor=W
        )
        # ------------------------------------------------------

    TelaInicial.mainloop()
