#!/usr/bin/env python3
import os
import subprocess
from time import sleep

def run():
	sleep(1)
	# -----------------------------------
	# percorrer caminho até pasta do time
	# -----------------------------------
	print("\n------------------------------")
	print("Time Reserva entrando em campo")
	print("------------------------------\n")
	input_ = 'cd && cd Documents/Reserva_AR/ && ./start.sh'
	os.system(input_)
	# if (os.system(input_) == 0):
	# 	# ----------------
	# 	# time encontrado
	# 	# ----------------
	# 	# iniciar time
	# 	# ----------------
	# 	input_ = './start.sh'
	# 	os.system(input_)