#!/usr/bin/env python3
import os
import subprocess

from time import sleep
import threading

import constants.constants as constants  

# from view.code import team1
# from view.code import team2
# from view.code import partida
# from view.code import monitor

def run(dict_config):

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

	t1 = threading.Thread(target=setParams).start()
	while t1.is_alive():
		print('T1 is alive')
		sleep(1)

	t2 = threading.Thread(target=config).start()
	while t2.is_alive():
		print('T2 is alive')
		sleep(1)

	return True