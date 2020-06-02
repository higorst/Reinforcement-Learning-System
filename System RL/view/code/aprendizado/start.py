# -*- coding: UTF-8 -*-
import os
import subprocess

from time import sleep
import threading

from view.code import team1
from view.code import team2
from view.code import partida
from view.code import monitor
from view.code import getPlacar as placar
from view.code import monitor

import constants.constants as constants
import random

def run(dicTeam):
	def partida_():
		partida.run(dicTeam["partida"])

	def time1():
		team1.run(dicTeam["team1"])

	def time2():
		team2.run(dicTeam["team2"])

	def monitor():
		monitor.run(dicTeam["monitor"])     

	input_ = constants.resetLogDir
	var = subprocess.getoutput(input_)
	
	t1 = threading.Thread(target=partida_)
	t1.start()
	sleep(0.5)
	t2 = threading.Thread(target=time1)
	t2.start()
	# para forçar times entrarem em campo nessa ordem
	sleep(1)
	t3 = threading.Thread(target=time2)
	t3.start()

	while t1.isAlive() or t2.isAlive() or t3.isAlive():
		sleep(1)

	return placar.run(1)
	# sleep(2)
	# return tuple([random.randint(5,7), random.randint(1,2)])
