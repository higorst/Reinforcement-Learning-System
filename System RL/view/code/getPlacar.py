#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
import os, glob            
import constants.constants as constants  

def run(ar = None):

	# ir até pasta log e pegar nome do arquivo log
	# para avisar que resultado pode ser coletado
	file = open(constants.fileFreedom, 'r')
	res = file.read()
	file.close()
	while res == "False":
		sleep(1)
		file = open(constants.fileFreedom, 'r')
		res = file.read()
		file.close()

	team1 = constants.ERROR
	team2 = constants.ERROR
	try:
		arq = glob.glob("*.rcl")[0]
		file_rcl = arq
		file_rcg = arq.replace('.rcl','.rcg')
		arq = arq.split('-vs-')
		team1 = arq[0]
		team2 = arq[1].replace('.rcl','')
		
		# placar 1
		done = False
		l = len(team1) - 1
		while not done:
			if ( team1[l] == '_' ):
				done = True
				team1 = team1[(l+1):len(team1)]
			l = l - 1

		# placar 2
		done = False
		l = len(team2) - 1
		while not done:
			if ( team2[l] == '_' ):
				done = True
				team2 = team2[(l+1):len(team2)]
			l = l - 1

		# mover arquivos de .log para log
		if ar == None:
			input_ = 'cd && mv /home/ufrbots/.log/' + file_rcl + ' /home/ufrbots/log'
			os.system(input_)
			input_ = 'cd && mv /home/ufrbots/.log/' + file_rcg + ' /home/ufrbots/log'
			os.system(input_)
		else:
			input_ = 'cd && mv /home/ufrbots/.log/' + file_rcl + ' /home/ufrbots/logAR'
			os.system(input_)
			input_ = 'cd && mv /home/ufrbots/.log/' + file_rcg + ' /home/ufrbots/logAR'
			os.system(input_)
	except Exception as e:
		print('Error 000')
		return tuple([constants.ERROR, constants.ERROR])

	return tuple([team1, team2])