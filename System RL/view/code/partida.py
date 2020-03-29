#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
import os            
import constants.constants as constants               

def run(mode):
	# ----------------------
	# (1) - iniciar server
	# ----------------------
	# modo rápido
	if (mode == constants.btModoMatchFast):
		input_ = "cd && cd log/ && rcssserver server::auto_mode = true server::nr_extra_halfs = 0 server::penalty_shoot_outs = false  server::synch_mode=true"
	# modo normal
	else:
		input_ = "cd && cd log/ && rcssserver"
	os.system(input_)

# --------------------------------------
# var = os.system("ls")
# if (var == 0 ):
# 	print("Deu certo!")
# else:
# 	print("Deu errado!")

# var = subprocess.getoutput("ifconfig")
# print("SAÍDA")
# print(var)
# --------------------------------------