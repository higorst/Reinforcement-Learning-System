#!/usr/bin/env python3
import os
import subprocess

from time import sleep
import threading

from view import popup as popup_
import constants.constants as constants  

# from view.code import team1
# from view.code import team2
# from view.code import partida
# from view.code import monitor

def run(dict_config, op):

	def sucess():
		msg = 'Sucesso'
		popup_.run(msg, 2000)

	def setParamsPopup():
		msg = 'Configurando Time de Aprendizado!\nAguarde ..'
		popup_.run(msg, 5000)

	def setParams():
		# SETAR CONFIGURAÇÕES PARA TIME AR_SYSTEM
		path = '/home/ufrbots/Documents/AR_System/src/PlayerTeams.cpp'
		file = open(path, 'r')

		new = ''
		for line in file:
		    l = line
		    if "float e_greedy =" in l:
		        l = "float e_greedy = " + str(dict_config["epsilon"]) + ";\n"
		    elif "float alpha =" in l:
		        l = "float alpha = " + str(dict_config["alpha"]) + ";\n"
		    elif "float gamma =" in l:
		        l = "float gamma = " + str(dict_config["gamma"]) + ";\n"
		    new += l

		file.close()

		f = open(path, 'w')
		f.write(new)
		f.close()
		# SETAR MATRIZ
		# ---- FALTA
		pass

	def configPopup():
		msg = 'Verificando configuração ...\n'
		popup_.run(msg, 2000)

	def config():
		# -----------
		# ./configure
		# -----------
		input_ = "cd && cd " + constants.addressDirAR + " && ./configure"
		var = subprocess.getoutput(input_)

		# -----------
		# make
		# -----------
		input_ = "cd && cd " + constants.addressDirAR + " && make"
		var = subprocess.getoutput(input_)
		pass	

	if op == 1:
		threading.Thread(target=setParamsPopup).start()
		t1 = threading.Thread(target=setParams)
		t1.start()
		while t1.isAlive():
			sleep(1)

	else:
		threading.Thread(target=configPopup).start()
		t2 = threading.Thread(target=config)
		t2.start()
		while t2.isAlive():
			sleep(1)
		threading.Thread(target=sucess).start()

	return True