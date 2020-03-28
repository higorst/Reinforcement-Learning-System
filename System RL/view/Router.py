# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import constants.constants as constants
import TelaInicial as telaInicial

from view import aprendizado
from view import resultados
from view import dados
from view import config
from view import about

def router(id, TelaInicial):

	lista = TelaInicial.winfo_children()
	for l in lista:
	    l.destroy()

	if  ( id == 0 ):
		# TelaInicial.destroy()
		telaInicial.TelaInicial(TelaInicial)
	elif( id == 1 ):
		aprendizado.view(TelaInicial)
	elif( id == 2 ):
		resultados.view(TelaInicial)
	elif( id == 3 ):
		dados.view(TelaInicial)
	elif( id == 4 ):
		config.view(TelaInicial)
	elif( id == 5 ):
		about.view(TelaInicial)

# messagebox.showinfo(
#     "Hello", 
#     id
# )