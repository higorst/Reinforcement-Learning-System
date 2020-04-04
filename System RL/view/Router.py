# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
import TelaInicial as telaInicial

import os

from view import partida
from view import aprendizado
from view import dados
from view import config
from view import about

def router(id, TelaInicial):

	# Apaga conteúdo da view
	lista = TelaInicial.winfo_children()
	for l in lista:
	    l.destroy()

	# Rotina para sair do sistema
	if( id == 999 ):
		# Apga diretórios __pycache__
		input_ = "rm -r /home/ufrbots/.System\ RL/__pycache__ && rm -r /home/ufrbots/.System\ RL/constants/__pycache__ && rm -r /home/ufrbots/.System\ RL//view/__pycache__ && rm -r /home/ufrbots/.System\ RL//view/code/__pycache__ && exit"
		os.system(input_)

		# Finaliza programa
		TelaInicial.destroy()
		TelaInicial.quit()

    # ------------------------------------------------------
    # Rotinas para chamar nova view
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Tela Inicial
    # ------------------------------------------------------
	elif( id == 0 ):
		telaInicial.TelaInicial(TelaInicial)

    # ------------------------------------------------------
	# Tela partida
    # ------------------------------------------------------
	elif( id == 1 ):
		partida.view(TelaInicial)

    # ------------------------------------------------------
	# Tela AR
    # ------------------------------------------------------
	elif( id == 2 ):
		aprendizado.view(TelaInicial)

    # ------------------------------------------------------
	# Tela dados
    # ------------------------------------------------------
	elif( id == 3 ):
		dados.view(TelaInicial)

    # ------------------------------------------------------
	# Tela config
    # ------------------------------------------------------
	elif( id == 4 ):
		config.view(TelaInicial)

    # ------------------------------------------------------
	# Tela sobre
    # ------------------------------------------------------
	elif( id == 5 ):
		about.view(TelaInicial)