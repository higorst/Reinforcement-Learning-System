# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
import TelaInicial as telaInicial

import os

from view import partida
from view import ar
from view import parametros
from view import dados
from view import partidasAR
from view import logplayer
from view import tutorial
from view import about

def router(id, TelaInicial, dict_ = None):

	# Apaga conteúdo da view
	lista = TelaInicial.winfo_children()
	for l in lista:
	    l.destroy()

	# Rotina para sair do sistema
	if( id == 999 ):
		# Apga diretórios __pycache__
		input_ = "rm -r /home/ufrbots/.log && mkdir /home/ufrbots/.log && rm -r /home/ufrbots/.System\ RL/__pycache__ && rm -r /home/ufrbots/.System\ RL/constants/__pycache__ && rm -r /home/ufrbots/.System\ RL/view/__pycache__ && rm -r /home/ufrbots/.System\ RL/view/code/__pycache__ && rm -r /home/ufrbots/.System\ RL/view/code/aprendizado/__pycache__ && exit"
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
		ar.view(TelaInicial)

	# ------------------------------------------------------
	# Tela AR - Parâmetros
    # ------------------------------------------------------
	elif( id == 21 ):
		parametros.view(TelaInicial, dict_)

	# ------------------------------------------------------
	# Tela AR - Partida
    # ------------------------------------------------------
	elif( id == 22 ):
		partidasAR.view(TelaInicial, dict_)

	# ------------------------------------------------------
	# Tela AR - Dados
    # ------------------------------------------------------
	elif( id == 23 ):
		dados.view(TelaInicial, dict_)

    # ------------------------------------------------------
	# Tela logplayer
    # ------------------------------------------------------
	elif( id == 3 ):
		logplayer.view(TelaInicial)

    # ------------------------------------------------------
	# Tela tutorial
    # ------------------------------------------------------
	elif( id == 4 ):
		tutorial.view(TelaInicial)

    # ------------------------------------------------------
	# Tela sobre
    # ------------------------------------------------------
	elif( id == 5 ):
		about.view(TelaInicial)