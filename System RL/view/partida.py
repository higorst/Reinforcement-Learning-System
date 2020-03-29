# -*- coding: UTF-8 -*-
from kinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants

from view import Router
from view.code import home

import info as Info

import os
from pathlib import Path

def view(TelaInicial):	

    # Nome dos times
    dictTeamName = {
        1 : "",
        2 : ""
    }

    # Path para cada time
    dictTeamPath = {
        1 : "",
        2 : ""
    }

    dictPartida = {
        "partida" : constants.btModoMatchNormal,
        "monitor" : constants.btModoViewActive,
    }

    def router(id):
        Router.router(id, TelaInicial)
        pass

    def reset():
        # Nome dos times
        dictTeamName[1] = ''
        dictTeamName[2] = ''

        # Path para cada time
        dictTeamPath[1] = ''
        dictTeamPath[2] = ''

        render()

    def stop():
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

    def start():
        dicTeam = {
            "partida" : str(dictPartida["partida"]),
            "monitor" : str(dictPartida["monitor"]),
            "team1" : {
                "teamName" : str(dictTeamName[1]),
                "path" : str(dictTeamPath[1])
            },
            "team2" : {
                "teamName" : str(dictTeamName[2]),
                "path" : str(dictTeamPath[2])
            }
        }
        home.run(dicTeam)
        # ------------------------------------------------------
        # Button Stop
        # ------------------------------------------------------
        btMenu = Button(
            TelaInicial, 
            width=76, 
            text=constants.btStop, 
            command=stop,
            bg=constants.buttonStopColor, 
            fg=constants.letterColor,
            activebackground=constants.buttonStopColorActive
        )
        btMenu.place(
            x=402, 
            y=579, 
            anchor=CENTER
        )

    def change(id):
        # modo
        if ( id == 1 ):
            if (dictPartida["partida"] == constants.btModoMatchNormal):
                dictPartida["partida"] = constants.btModoMatchFast
            else:
                dictPartida["partida"] = constants.btModoMatchNormal
        # monitor
        else:
            if (dictPartida["monitor"] == constants.btModoViewActive):
                dictPartida["monitor"] = constants.btModoViewInactive
            else:
                dictPartida["monitor"] = constants.btModoViewActive
        renderConfigMatch(id)

    def info():
        os.system(constants.openInfoOsSytem)
        pass

    def getTeam(id):
        TelaInicial.directory = filedialog.askdirectory(
            initialdir = constants.initialDirectory,
            title = constants.titleAskDirectory
        )
        # Armazena path
        dictTeamPath[id] = TelaInicial.directory

        # Rotina para acessar arquivo star.sh
        # para pegar nome do time
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

    def renderConfigMatch(id):
        # ------------------------------------------------------
        # Configurações de partida - INÍCIO
        # ------------------------------------------------------
        if ( id == 1 ):
            bt = Button(
                TelaInicial, 
                width=15, 
                text=dictPartida["partida"], 
                command=lambda change=change: change(1),
                bg=constants.buttonColorConfig, 
                fg=constants.letterColor,
                activebackground=constants.activeButtonColor
            )
            bt.place(
                x=200, 
                y=340, 
                anchor=CENTER
            )
        # ------------------------------------------------------

        # ------------------------------------------------------
        if ( id == 2 ):
            bt = Button(
                TelaInicial, 
                width=15, 
                text=dictPartida["monitor"], 
                command=lambda change=change: change(2),
                bg=constants.buttonColorConfig, 
                fg=constants.letterColor,
                activebackground=constants.activeButtonColor
            )
            bt.place(
                x=200, 
                y=390, 
                anchor=CENTER
            )
        # ------------------------------------------------------
        # Configurações de partida - FIM
        # ------------------------------------------------------

    def render():
        # Apaga conteúdo da view
        lista = TelaInicial.winfo_children()
        for l in lista:
            l.destroy()

        # ------------------------------------------------------
        # Definições da view
        TelaInicial.title(
            constants.titleTela01
        )
        TelaInicial.configure(
            background=constants.backgroundColor
        )

        if (dictTeamName[1] != '' and dictTeamName[2] != ''):
            # ------------------------------------------------------
            # Image Versus
            # ------------------------------------------------------
            width = int(1176 / constants.proportionVSImage)
            height = int(1004 / constants.proportionVSImage)
            img = Image.open(constants.addressVS)
            img = img.resize((width,height), Image.ANTIALIAS)
            vs = ImageTk.PhotoImage(img)
            panel = Label(TelaInicial, image=vs, bg=constants.backgroundColor)
            panel.place(x=400, y=40, anchor=N)
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
                constants.fontPersonalizadaTeam, 
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
                constants.fontPersonalizadaTeam, 
                constants.fontSizeTeamName
            )
        )
        lbTeam02.place(
            x=constants.xLenghtLabelTeam + 300, 
            y=100, 
            anchor=CENTER
        )
        # ------------------------------------------------------
        if not (dictTeamName[1] != '' and dictTeamName[2] != ''):
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
        # Button - escolher novamente os times
        else:
            icon = PhotoImage(file = constants.addressRefresh)
            bt = Button(
                TelaInicial, 
                width=30, 
                image=icon, 
                command=reset,
                bg=constants.backgroundColor, 
                fg=constants.letterColor,
                activebackground=constants.activeButtonColor
            )
            bt.config(highlightbackground=constants.buttonHighLight)
            bt.place(
                x=10, 
                y=10, 
                anchor=NW
            )

        renderConfigMatch(1)
        renderConfigMatch(2)

        # ------------------------------------------------------
        # Footbal Image
        # ------------------------------------------------------
        width = 200
        height = 200
        img = Image.open(constants.addressFootbalField)
        img = img.resize((width,height), Image.ANTIALIAS)
        foot = ImageTk.PhotoImage(img)
        panel = Label(TelaInicial, image=foot, bg=constants.backgroundColor)
        panel.place(x=600, y=360, anchor=CENTER)
        # ------------------------------------------------------

        if (dictTeamName[1] == '' or dictTeamName[2] == ''):
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
        else:
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
