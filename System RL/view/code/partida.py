#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
import os, glob            
import constants.constants as constants  

def run(mode):
	# criar página .log
	os.system(constants.createLogDir)

	# para avisar que resultado ainda não pode ser coletado
	file = open(constants.fileFreedom, 'w')
	file.write('False')
	file.close()

	# ----------------------
	# (1) - iniciar server
	# ----------------------

	# modo rápido
	if (mode == constants.btModoMatchFast):
		input_ = "cd && cd .log/ && rcssserver server::auto_mode = true server::nr_extra_halfs = 0 server::penalty_shoot_outs = false  server::synch_mode=true"
	# modo normal
	else:
		input_ = "cd && cd .log/ && rcssserver"
	var = subprocess.getoutput(input_)

	sleep(12)
	os.chdir("/home/ufrbots/.log")
	
	while glob.glob("*.rcl") == []:
		print('NOT FIND - PARTIDA')
		sleep(1)

	arq = glob.glob("*.rcl")[0]
	cte = 0
	while arq == "incomplete.rcl" and cte < 20:
		print('INCOMPLETE - PARTIDA')
		sleep(1)
		cte = cte + 1
		arq = glob.glob("*.rcl")[0]

	# para avisar que resultado pode ser coletado
	file = open(constants.fileFreedom, 'w')
	file.write('True')
	file.close()