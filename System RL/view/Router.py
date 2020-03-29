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
		input_ = "rm -r __pycache__ "+
		"&& constants/__pycache__ "+
		"&& img/__pycache__ "+
		"&& view/__pycache__ "+
		"&& view/code/__pycache__"
		os.system(input_)

		# Finaliza programa
		TelaInicial.destroy()
		TelaInicial.quit()

    # Rotinas para chamar nova view
	elif( id == 0 ):
		telaInicial.TelaInicial(TelaInicial)
	elif( id == 1 ):
		partida.view(TelaInicial)
	elif( id == 2 ):
		aprendizado.view(TelaInicial)
	elif( id == 3 ):
		dados.view(TelaInicial)
	elif( id == 4 ):
		config.view(TelaInicial)
	elif( id == 5 ):
		about.view(TelaInicial)