# -*- coding: UTF-8 -*-
import os
import subprocess

from time import sleep
import threading

from view.code import team1
from view.code import team2
from view.code import partida
from view.code import monitor

def run(dicTeam):
	def partida():
		partida.run(dicTeam["partida"])

	def time1():
		team1.run(dicTeam["team1"])

	def time2():
		team2.run(dicTeam["team2"])     

	def monitor():
		monitor.run(dicTeam["monitor"])

	threading.Thread(target=partida).start()
	threading.Thread(target=time1).start()
	threading.Thread(target=time2).start()
	threading.Thread(target=monitor).start()

	# aguarda tempo da partida
	sleep(170)

# --------------------------------------
# var = subprocess.getoutput("ifconfig")
# --------------------------------------