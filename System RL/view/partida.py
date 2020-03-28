# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants
from view import Router
import info as Info

import os
from pathlib import Path

def view(TelaInicial):	

    dictTeamName = {
        1 : "",
        2 : ""
    }

    def router(id):
        Router.router(id, TelaInicial)
        pass

    def info():
        os.system(constants.openInfoOsSytem)
        pass

    def getTeam(id):
        TelaInicial.directory = filedialog.askdirectory(
            initialdir = constants.initialDirectory,
            title = constants.titleAskDirectory
        )
        data_folder = Path(TelaInicial.directory)
        file_to_open = data_folder / constants.archiveToReadTeam

        f = open(
            file_to_open, 
            'r'
        )
        for line in f:
            if ( line[0:12] == constants.stringForNameTeam ):
                dictTeamName[id] = line[13:len(line)].replace("\"","")
                dictTeamName[id] = dictTeamName[id].replace(" ","")
        render()

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
        # Image Versus
        # ------------------------------------------------------
        width = int(1176 / constants.proportionVSImage)
        height = int(1004 / constants.proportionVSImage)
        img = Image.open(constants.addressVS)
        img = img.resize((width,height), Image.ANTIALIAS)
        vs = ImageTk.PhotoImage(img)
        panel = Label(TelaInicial, image=vs, bg=constants.backgroundColor)
        panel.place(x=400, y=170, anchor=CENTER)
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Label Team 01
        # ------------------------------------------------------
        lbTeam01 = Label(
            TelaInicial, 
            width=constants.widthLabelTeam, 
            text=dictTeamName[1], 
            bg=constants.backgroundColor,
            fg=constants.letterColor
        )    
        lbTeam01.config(
            font=(
                constants.fontPersonalizada, 
                constants.fontSizeTeamName
            )
        )
        lbTeam01.place(
            x=constants.xLenghtLabelTeam, 
            y=100, 
            anchor=CENTER
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Label Team 02
        # ------------------------------------------------------
        lbTeam02 = Label(
            TelaInicial, 
            width=constants.widthLabelTeam, 
            text=dictTeamName[2], 
            bg=constants.backgroundColor,
            fg=constants.letterColor
        )    
        lbTeam02.config(
            font=(
                constants.fontPersonalizada, 
                constants.fontSizeTeamName
            )
        )
        lbTeam02.place(
            x=constants.xLenghtLabelTeam + 300, 
            y=100, 
            anchor=CENTER
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Button Get Team 01
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.widthLabelTeam, 
            text=constants.btGetTeam01, 
            command=lambda getTeam=getTeam: getTeam(1), 
            bg=constants.butonColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor,
        )
        bt.place(
            x=constants.xLenghtLabelTeam, 
            y=150, 
            anchor=CENTER
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Button Get Team 02
        # ------------------------------------------------------
        bt = Button(
            TelaInicial, 
            width=constants.widthLabelTeam, 
            text=constants.btGetTeam02, 
            command=lambda getTeam=getTeam: getTeam(2), 
            bg=constants.butonColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor,
        )
        bt.place(
            x=(constants.xLenghtLabelTeam + 300), 
            y=150, 
            anchor=CENTER
        )
        # ------------------------------------------------------

        # ------------------------------------------------------
        # Button Info
        # ------------------------------------------------------
        btMenu = Button(
            TelaInicial, 
            width=5, 
            text=constants.btInfo, 
            command=info,
            bg=constants.butonColor, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColor
        )
        btMenu.place(
            x=725, 
            y=595, 
            anchor=SE
        )
        # ------------------------------------------------------

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

    render()
