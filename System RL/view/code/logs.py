#!/usr/bin/env python3
import os
import subprocess

from sys import exit

from time import sleep 
import os, glob            
import constants.constants as constants  

def run():

	logs = []
	show = []

	os.chdir("/home/ufrbots/logAR")
	for item in glob.glob("*.rcg"):
		logs.append(item)

		# placar - início
		arq = item
		arq = arq.split('-vs-')
		team1 = arq[0]
		team2 = arq[1].replace('.rcg','')
		
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
		# placar - fim
		item = item.replace(".rcg", "")
		item = item.replace(
			item[0:14], 
			"        " + item[0:4] + "/" + item[4:6] + "/" + item[6:8] + "             -             " +
			item[8:10] + "h:" + item[10:12] + "min:" + item[12:14] + "s "
			)
		item = item[0:58]

		team1 = str(team1)
		team2 = str(team2)
		if len(team1) < 2:
			team1 = " " + team1
		if len(team2) < 2:
			team2 += " "

		item += "             -             AR  " + team1 + " x " + team2 + "  Reserva"
		show.append(item)

	return tuple([logs, show])