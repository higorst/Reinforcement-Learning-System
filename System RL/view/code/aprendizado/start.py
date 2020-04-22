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

import random

def run(dicTeam):
	def partida_():
		partida.run(dicTeam["partida"])

	def time1():
		team1.run(dicTeam["team1"])

	def time2():
		team2.run(dicTeam["team2"])     

	# input_ = "cd && rm -r /home/ufrbots/.log && mkdir /home/ufrbots/.log"
	# var = subprocess.getoutput(input_)
	
	# t1 = threading.Thread(target=partida_)
	# t1.start()
	# sleep(1)
	# t2 = threading.Thread(target=time1)
	# t2.start()
	# # para forçar times entrarem em campo nessa ordem
	# sleep(1)
	# t3 = threading.Thread(target=time2)
	# t3.start()

	# while t1.isAlive() or t2.isAlive() or t3.isAlive():
	# 	sleep(1)

	# return placar.run(1)
	return tuple([random.randint(2,5), random.randint(0,1)])
