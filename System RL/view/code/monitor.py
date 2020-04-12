#!/usr/bin/env python3
import os
import subprocess

from time import sleep 
from sys import exit
import os                  
import constants.constants as constants          

def run(mode):
	# ----------------------
	# (1) - iniciar monitor
	# ----------------------
	if (mode == constants.btModoViewActive):
		input_ = "cd && rcssmonitor"
		os.system(input_)
		sleep(5)
		exit()
	else:
		pass