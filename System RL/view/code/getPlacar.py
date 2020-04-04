#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
import os, glob            
import constants.constants as constants  

def run():

	# ir até pasta log e pegar nome do arquivo log
	os.chdir("/home/ufrbots/.log")
	while glob.glob("*.rcl") == []:
		sleep(1)

	arq = glob.glob("*.rcl")[0]
	cte = 0
	while arq == "incomplete.rcl" and cte < 20:
		sleep(1)
		cte = cte + 1
		arq = glob.glob("*.rcl")[0]

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
	input_ = 'cd && mv /home/ufrbots/.log/' + file_rcl + ' /home/ufrbots/log'
	os.system(input_)
	input_ = 'cd && mv /home/ufrbots/.log/' + file_rcg + ' /home/ufrbots/log'
	os.system(input_)

	return tuple([team1, team2])