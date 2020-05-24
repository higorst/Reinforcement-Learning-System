#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
from sys import exit
import os                  
import constants.constants as constants          

def run(mode, partida=None):
	# ----------------------
	# (1) - iniciar monitor
	# ----------------------
	if (mode == constants.btModoViewActive):
		if partida == 1:
			input_ = "cd && rcssmonitor"
			os.system(input_)
		else:
			input_ = "cd && rcssmonitor --auto-reconnect-mode on"
			os.system(input_)
	else:
		pass