# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


import tkinter.font as tkFont
import tkinter.ttk as ttk

from time import sleep
import threading
import os, glob            

import constants.constants as constants
from view import Router
from view import popup as popup_

from view.code.aprendizado import configAR
from view.bd import query

from view.code import graph

def view(TelaInicial, dict_config):  

    resultados = query.getDados(dict_config["experimento_id"])
    ensaios = query.getEnsaios(dict_config["experimento_id"])

    def remover_ensaio():
        line = tree2.index(tree2.focus())
        if str(tree2.focus()) == "":
            popup("Selecione um ensaio!")
        else:
            query.deletarEnsaio(dict_config["experimento_id"], ensaios[line][5], ensaios[line][7], ensaios[line][8], ensaios[line][9])
            update()
            popup("Ensaio Removido com Sucesso!")

    def open_file(results_r1, results_r2):
        # placares gerais AR x RESERVA
        arq_results = open('.placares.txt', 'w');
        arq_results.write('Placares das Partidas \n(AR) x (Reserva)\n\n')
        for x in range(0, len(results_r1)):
            arq_results.write(str(results_r1[x]) + ' x ' + str(results_r2[x]) + '\n')
        arq_results.close()

        

        # Resultados apenas AR
        arq_results = open('.Gols_AR.txt', 'w');
        # arq_results.write('Resultados -> (AR)\n\n')
        for x in range(0, len(results_r1)):
            arq_results.write(str(results_r1[x]) + '\n')
        arq_results.close()

        

        # Resultados apenas RESERVA
        arq_results = open('.Gols_Reserva.txt', 'w');
        # arq_results.write('Resultados -> (Reserva)\n\n')
        for x in range(0, len(results_r2)):
            arq_results.write(str(results_r2[x]) + '\n')
        arq_results.close()

        input_ = 'gedit .placares.txt .Gols_AR.txt .Gols_Reserva.txt'
        os.system(input_)

    def results():
        line = tree2.index(tree2.focus())
        if str(tree2.focus()) == "":
            popup("Selecione um ensaio!")
        else:
            golsFeitos, golsSofridos, saldoGols, episodios = query.getFullEnsaio(ensaios[line][5])

            threading.Thread(target=lambda open_file=open_file: open_file(golsFeitos, golsSofridos)).start()
            graph.open(episodios, golsFeitos, golsSofridos, saldoGols, ensaios[line][7], ensaios[line][8], ensaios[line][9], ensaios[line][0], ensaios[line][10], ensaios[line][1])

    def update():
        global resultados
        global ensaios
        resultados = query.getDados(dict_config["experimento_id"])      
        ensaios = query.getEnsaios(dict_config["experimento_id"])

        # ---- tabela de combinações
        # limpar listbox
        for r in tree.get_children():
            tree.delete(r)
        for item in resultados:
            tree.insert('', 'end', values=item)

        # ---- tabela de ensaios
        # limpar listbox
        for r in tree2.get_children():
            tree2.delete(r)
        for item in ensaios:
            tree2.insert('', 'end', values=item)

    def popup(s):
        popup_.run(s)

    def router(id, dict_config = None):
        Router.router(id, TelaInicial)

    def show():
        # graph.run(dict_config)
        numEnsaios = query.getMAXofEnsaios(dict_config["experimento_id"])
        numCombinacoes = query.getCombinacoes(dict_config["experimento_id"])
        resultados = query.getDados(dict_config["experimento_id"])

        combinacoes = []
        i = 1
        for x in resultados:
            # comb = str("TA:"+x[1]+" FD:"+x[2]+" EG:"+x[3])
            comb = str("C"+str(i))
            combinacoes.append(comb)
            i += 1

        medias_saldo_de_gols = []
        medias_gols_feitos = []
        medias_gols_sofridos = []
        for x in resultados:
            medias_gols_feitos.append(x[1])
            medias_gols_sofridos.append(x[2])
            medias_saldo_de_gols.append(x[3])

        bar_width = 0.25
        y_pos = np.arange(len(combinacoes))

        fig, ax1 = plt.subplots(1)
        fig.tight_layout()

        gp1 = ax1.bar(y_pos-bar_width, medias_gols_feitos, bar_width, label=constants.labelGRAPH_AR, color='g', align='center', alpha=0.5, edgecolor='none')
        gp2 = ax1.bar(y_pos, medias_gols_sofridos, bar_width, label=constants.labelGRAPH_Res, color='r', align='center', alpha=0.5, edgecolor='none')
        gp3 = ax1.bar(y_pos+bar_width, medias_saldo_de_gols, bar_width, label=constants.labelGRAPH_Saldo, color='b', align='center', alpha=0.5, edgecolor='none')

        def autolabel(gps):
            """Attach a text label above each bar in *gp*, displaying its height."""
            for gp in gps:
                height = gp.get_height()
                ax1.annotate('{}'.format(height).replace(".0", ""),
                            xy=(gp.get_x() + gp.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom',
                            fontsize=15)

        autolabel(gp1)
        autolabel(gp2)
        autolabel(gp3)

        ax1.set_xticks(y_pos)
        ax1.set_xticklabels(combinacoes)
        ax1.legend(
            loc='upper center', 
            bbox_to_anchor=(0.5, 1.06), 
            fancybox=True, 
            shadow=True, 
            fontsize=15,
            ncol=3)

        plt.show()

    desc = "Experimento: " + dict_config["experimento_titulo"]
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
            14
        )
    )
    lbPartida.place(
        x=400, 
        y=15,
        anchor=N
    )

    if (len(resultados) > 0):
        # ----- TABELA DE COMBINAÇÕES
        container = ttk.Frame()
        container.place(x=10, y=50, width=780, height=120)
        titulos_listbox = ['[C] Combinação', '[MÉDIA] Gols Feitos', '[MÉDIA] Gols Sofridos', '[MÉDIA] Saldo de Gols', 'Taxa de Aprendizado', 'Fator de Desconto', 'Política e-greedy']
        # create a treeview with dual scrollbars
        tree = ttk.Treeview(columns=titulos_listbox, show="headings")
        vsb = ttk.Scrollbar(
            orient="vertical",
            command=tree.yview
            )
        hsb = ttk.Scrollbar(
            orient="horizontal",
            command=tree.xview
            )
        tree.configure(
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
            )
        tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        for col in titulos_listbox:
            tree.heading(col, text=col.title())
            # adjust the column's width to the header string
            tree.column(col,
                width=tkFont.Font().measure(col.title()))

        # ----- TABELA DE ENSAIOS
        container2 = ttk.Frame()
        container2.place(x=10, y=210, width=780, height=350)
        titulos_listbox = ['Combinação', 'Ensaio', '[SOMA] Gols Feitos', '[SOMA] Gols Sofridos', '[SOMA] Saldo de Gol']
        # create a treeview with dual scrollbars
        tree2 = ttk.Treeview(columns=titulos_listbox, show="headings")
        vsb = ttk.Scrollbar(
            orient="vertical",
            command=tree2.yview
            )
        hsb = ttk.Scrollbar(
            orient="horizontal",
            command=tree2.xview
            )
        tree2.configure(
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
            )
        tree2.grid(column=0, row=0, sticky='nsew', in_=container2)
        vsb.grid(column=1, row=0, sticky='ns', in_=container2)
        hsb.grid(column=0, row=1, sticky='ew', in_=container2)
        container2.grid_columnconfigure(0, weight=1)
        container2.grid_rowconfigure(0, weight=1)

        for col in titulos_listbox:
            tree2.heading(col, text=col.title())
            # adjust the column's width to the header string
            tree2.column(col,
                width=tkFont.Font().measure(col.title()))
        update()

        # ------------------------------------------------------
        # Button Média de Saldos
        # ------------------------------------------------------
        btMenu = Button(
            TelaInicial, 
            width=94, 
            text="Médias das Combinações", 
            command=show,
            bg=constants.butonColorInfo, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColorInfo
        )
        btMenu.place(
            x=400, 
            y=190, 
            anchor=CENTER
        )
        # ------------------------------------------------------
        # ------------------------------------------------------
        # Button Resultados
        # ------------------------------------------------------
        btMenu = Button(
            TelaInicial, 
            width=36, 
            text="Remover Ensaio", 
            command=remover_ensaio,
            bg=constants.buttonStopColor, 
            fg=constants.letterColor,
            activebackground=constants.buttonStopColorActive
        )
        btMenu.place(
            x=242, 
            y=581, 
            anchor=CENTER
        )
        # ------------------------------------------------------
        # Button Resultados
        # ------------------------------------------------------
        btMenu = Button(
            TelaInicial, 
            width=36, 
            text="Ver Ensaio", 
            command=results,
            bg=constants.butonColorInfo, 
            fg=constants.letterColor,
            activebackground=constants.activeButtonColorInfo
        )
        btMenu.place(
            x=565, 
            y=581, 
            anchor=CENTER
        )
    # ------------------------------------------------------
    else:
        # ------------------------------------------------------
        lb = Label(
            TelaInicial, 
            text="Nenhum aprendizado realizado para este experimento!\n\n\nExecute pelo menos 1 ensaio e retorne para analisar os dados!", 
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
            x=225, 
            y=300,
            anchor=W
        )
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

    TelaInicial.mainloop()
