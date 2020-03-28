#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
import os                           

def run():
	# ----------------------
	# (1) - iniciar server
	# ----------------------
	input_ = "cd && cd log/ && rcssserver server::auto_mode = true server::nr_extra_halfs = 0 server::penalty_shoot_outs = false  server::synch_mode=true"
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