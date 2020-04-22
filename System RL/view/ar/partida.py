# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import random

import constants.constants as constants

from view import Router
from view import popup as popup_
from view.code import home
from view.code import getPlacar as placar

from view.code.aprendizado import start as start_

from view.code import graph

import info as Info

from time import sleep 
import threading
import os, glob            
from pathlib import Path

def view(TelaInicial, dict_config):

    results_r1 = []
    results_r2 = []
    results_saldo = []
    graph_x = []

    def popup(s):
        popup_.run(s)

    def router(id):
        Router.router(id, TelaInicial)
        pass

    def openFile():
    	# placares gerais AR x RESERVA
        arq_results = open('.results.txt', 'w');
        arq_results.write('Placares das Partidas \n(AR) x (Reserva)\n\n')
        for x in range(0, len(results_r1)):
            arq_results.write(str(results_r1[x]) + ' x ' + str(results_r2[x]) + '\n')
        arq_results.close()

        

        # Resultados apenas AR
        arq_results = open('.ResultadosAR.txt', 'w');
        # arq_results.write('Resultados -> (AR)\n\n')
        for x in range(0, len(results_r1)):
            arq_results.write(str(results_r1[x]) + '\n')
        arq_results.close()

        

        # Resultados apenas RESERVA
        arq_results = open('.ResultadosReserva.txt', 'w');
        # arq_results.write('Resultados -> (Reserva)\n\n')
        for x in range(0, len(results_r2)):
            arq_results.write(str(results_r2[x]) + '\n')
        arq_results.close()

        input_ = 'gedit .results.txt .ResultadosAR.txt .ResultadosReserva.txt'
        os.system(input_)

    def openGraph():
        graph.open(graph_x, results_r1, results_r2, results_saldo)

    def results():
        threading.Thread(target=openFile).start()
        openGraph()

    def verify():
        if dict_config["started"] and int(dict_config["episode"]) <= int(dict_config["episodes"]):
            start()
        else:
            countMatch(1, 1)
            # ------------------------------------------------------
            # Button Start
            # ------------------------------------------------------
            btMenu = Button(
                TelaInicial, 
                width=76, 
                text=constants.btBeforeAR, 
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

    def start():
        if not dict_config["started"]:
            # results_r1.clear()
            # results_r2.clear()
            # results_saldo.clear()
            # graph_x.clear()
            dict_config["started"] = True
            # ------------------------------------------------------
            # Button Start
            # ------------------------------------------------------
            btMenu = Button(
                TelaInicial, 
                width=76, 
                text=constants.btAfterAguarde, 
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
        else:
            while(dict_config["started"] and int(dict_config["episode"]) <= int(dict_config["episodes"])):
                dicTeam = {
                    "partida" : constants.btModoMatchFast,
                    "team1" : {
                        "teamName" : constants.addressTeamArName,
                        "path" : constants.addressTeamArSystem
                    },
                    "team2" : {
                        "teamName" : constants.addressTeamResName,
                        "path" : constants.addressTeamResSystem
                    }
                }
                countMatch(dict_config["episode"])
                TelaInicial.update_idletasks()

                r1, r2 = start_.run(dicTeam)
                if r1 != constants.ERROR and r2 != constants.ERROR:

                    results_r1.append(int(r1))
                    results_r2.append(int(r2))
                    results_saldo.append(int(r1)-int(r2))
                    graph_x.append(int(dict_config["episode"]))

                    graphLive()
                    progress_bar.set(int(dict_config["episode"]))

                    ep = str(dict_config["episode"])
                    r1 = str(r1)
                    r2 = str(r2)

                    while len(ep) < 3:
                        ep += ' '
                    while len(r1) < 2:
                        r1 += ' '
                    while len(r2) < 2:
                        r2 += ' '

                    listbox_1.insert(END, " Partida " + ep)
                    listbox_2.insert(END, r1)
                    listbox_3.insert(END, r2)

                    listbox_1.see(listbox_1.size())
                    listbox_2.see(listbox_2.size())
                    listbox_3.see(listbox_3.size())
                    dict_config["episode"] += 1
                else:
                    popup_.run(constants.msgReiniciarPartida, 2000)
                TelaInicial.update_idletasks()

        TelaInicial.update_idletasks()
        TelaInicial.after_idle(verify())

    def countMatch(x, final = None):
        if final == None:
            desc = "Partida " + str(x) + " em andamento"
        else:
            desc = "        Episódios completos        "
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
            y=20,
            anchor=N
        )
        # ------------------------------------------------------

    def graphLive():
        data1 = {'Partida': graph_x,
                 'Saldo_de_Gol': results_saldo
                }
        df1 = DataFrame(data1,columns=['Partida','Saldo_de_Gol'])
        df2 = df1[['Partida','Saldo_de_Gol']].groupby('Partida').sum()
        df2.plot(kind='line', legend=False, ax=ax2, color='r',marker='o', linewidth=1, linestyle='dashed')

        figure2.canvas.draw()
        figure2.canvas.flush_events()

    data1 = {'Partida': graph_x,
             'Saldo_de_Gol': results_saldo
            }
    df1 = DataFrame(data1,columns=['Partida','Saldo_de_Gol'])

    figure2 = plt.Figure(figsize=(19,4), dpi=50, facecolor='white', edgecolor='white')
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, TelaInicial)
    line2.get_tk_widget().place(
        x=390, 
        y=370,
        anchor=N
    )
    df2 = df1[['Partida','Saldo_de_Gol']].groupby('Partida').sum()
    # df2.plot(kind='line', legend=False, ax=ax2, color='w',marker='', linewidth=0, linestyle='dashed')
    ax2.tick_params(top='off', bottom='off', left='off', right='off', labelright=True)
    ax2.set_title('Saldo de Gols')
    ax2.set_xlabel('')

    # AR x Reserva
    Label(
        TelaInicial, 
        text=constants.labelResultTeam,
        bg=constants.backgroundColor,
        font=constants.fontPersonalizadaList,
    ).place(
        x=530, 
        y=90, 
        anchor=W
    )
    # Resultados
    Label(
        TelaInicial, 
        text=constants.labelResult,
        bg=constants.backgroundColor,
        font=constants.fontPersonalizadaList,
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
        font=constants.fontPersonalizadaList,
        fg=constants.listboxFG,
        bg=constants.listboxBG,
        bd=0,
    )
    listbox_1.configure(justify=CENTER)
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
        font=constants.fontPersonalizadaList,
        fg=constants.listboxFG,
        bg=constants.listboxBG,
        bd=0,
    )
    listbox_2.configure(justify=CENTER)
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
        font=constants.fontPersonalizadaList,
        fg=constants.listboxFG,
        bg=constants.listboxBG,
        bd=0,
    )
    listbox_3.configure(justify=CENTER)
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
        length=744,
        variable=progress_bar, 
        orient="horizontal", 
        maximum=int(dict_config["episodes"]),
    )
    barra.place(
        x=402, 
        y=350,
        anchor=N
    )

    dist_x = 115
    # Algorithm
    Label(
        TelaInicial, 
        text=constants.labelAlgorithm,
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=100, 
        anchor=W
    )
    # Alpha
    Label(
        TelaInicial, 
        text=constants.labelAlpha,
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=130, 
        anchor=W
    )
    # Gamma
    Label(
        TelaInicial, 
        text=constants.labelGamma,
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=160, 
        anchor=W
    )
    # Epsilon
    Label(
        TelaInicial, 
        text=constants.labelEpsilon,
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=190, 
        anchor=W
    )
    # Episodes
    Label(
        TelaInicial, 
        text=constants.labelEpisodes,
        bg=constants.backgroundColor
    ).place(
        x=dist_x, 
        y=220, 
        anchor=W
    )

    dist_x = 250
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

    dist_x = 270
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
        text=constants.btAfterAR, 
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

    TelaInicial.mainloop()
