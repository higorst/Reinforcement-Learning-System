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

import info as Info

from time import sleep 
import threading
import os, glob            
from pathlib import Path

def open(graph_x, results_r1, results_r2, results_saldo):
    plt.plot(graph_x, results_r1, 'go-', label=constants.labelGRAPH_AR, linewidth=1, linestyle='dashed')
    plt.plot(graph_x, results_r2, 'bo-', label=constants.labelGRAPH_Res, linewidth=1, linestyle='dashed')
    plt.plot(graph_x, results_saldo, 'ro-', label=constants.labelGRAPH_Saldo, linewidth=1, linestyle='dashed')
    plt.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, -0.02), 
        fancybox=True, 
        shadow=True, 
        ncol=3)
    plt.show()