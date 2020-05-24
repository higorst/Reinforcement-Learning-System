#!/usr/bin/env python3
import os
import subprocess

from time import sleep
import threading

from view import popup as popup_
import constants.constants as constants  

def run(dict_config, op):

	num_states = 30
	num_actions = 5

	def sucess():
		msg = constants.msgSucess
		popup_.run(msg, 1000)

	def setParamsPopup():
		msg = constants.msgSetParms
		popup_.run(msg, 2000)
		if int(dict_config["matriz"]) == 2:
			msg = constants.msgCriarMatriz
			popup_.run(msg, 2000)

	def setParams():
		# SETAR CONFIGURAÇÕES PARA TIME AR_SYSTEM
		path = constants.addressFilePlayerTeams
		file = open(path, 'r')

		new = ''
		for line in file:
		    l = line
		    if "#define e_greedy" in l:
		        l = "#define e_greedy " + str(dict_config["epsilon"]) + "\n"
		    elif "#define alpha" in l:
		        l = "#define alpha " + str(dict_config["alpha"]) + "\n"
		    elif "#define gamma" in l:
		        l = "#define gamma " + str(dict_config["gamma"]) + "\n"
		    new += l

		file.close()

		f = open(path, 'w')
		f.write(new)
		f.close()
		# SETAR MATRIZ
		if int(dict_config["matriz"]) == 2:
			path = constants.addressFileMatriz
			f_ = open(path, 'w')
			for i in range(0,num_states):
				for j in range(0,num_actions):
					f_.write("0.00")
					if j < 5:
						f_.write(" ")
				f_.write("\n")
			f_.close()

	def configPopup():
		msg = constants.msgConfigTeam
		popup_.run(msg, 8000)

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
		print(var)

	if op == 1:
		setParamsPopup()
		t1 = threading.Thread(target=setParams)
		t1.start()
		while t1.isAlive():
			sleep(1)

	else:
		configPopup()
		t2 = threading.Thread(target=config)
		t2.start()
		while t2.isAlive():
			sleep(1)
		threading.Thread(target=sucess).start()

	return True