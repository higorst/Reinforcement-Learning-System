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
	def partida_():
		partida.run(dicTeam["partida"])

	def time1():
		team1.run(dicTeam["team1"])

	def time2():
		team2.run(dicTeam["team2"])     

	def monitor_():
		monitor.run(dicTeam["monitor"], 1)

	input_ = "cd && rm -r /home/ufrbots/.log && mkdir /home/ufrbots/.log"
	var = subprocess.getoutput(input_)

	threading.Thread(target=partida_).start()
	sleep(1)
	threading.Thread(target=time1).start()
	# para forçar times entrarem em campo nessa ordem
	sleep(2)
	threading.Thread(target=time2).start()
	threading.Thread(target=monitor_).start()

# --------------------------------------
# var = subprocess.getoutput("ifconfig")
# --------------------------------------