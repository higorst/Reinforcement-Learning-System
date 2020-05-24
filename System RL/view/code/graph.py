# -*- coding: UTF-8 -*-
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

import info as Info

from time import sleep 
import threading
import os, glob            
from pathlib import Path

def open(graph_x, results_r1, results_r2, results_saldo, alpha=None, gamma=None, epsilon=None, combinacao=None, episodios=None, ensaio=None):

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.tight_layout()

    if combinacao is not None:
        ax1.set_title("Combinação: " + str(combinacao) + "           Ensaio: " + str(ensaio) + "          Nº Episódios: " + str(episodios))
        # ax1.set_title("[Taxa de Aprendizado: " + str(alpha) + " Fator de Desconto: " + str(gamma) + " Política e-greedy: " + str(epsilon) + "] Combinação: " + str(combinacao) + "           Ensaio: " + str(ensaio) + "          Nº Episódios: " + str(episodios))

    ax1.plot(graph_x, results_r1, 'go-', label=constants.labelGRAPH_AR, linewidth=1, linestyle='dashed')
    ax1.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.05), 
        fancybox=True, 
        shadow=True, 
        ncol=1)

    ax2.plot(graph_x, results_r2, 'bo-', label=constants.labelGRAPH_Res, linewidth=1, linestyle='dashed')
    ax2.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.05), 
        fancybox=True, 
        shadow=True, 
        ncol=1)

    ax3.plot(graph_x, results_saldo, 'ro-', label=constants.labelGRAPH_Saldo, linewidth=1, linestyle='dashed')
    ax3.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.05), 
        fancybox=True, 
        shadow=True, 
        ncol=1)

    plt.show()