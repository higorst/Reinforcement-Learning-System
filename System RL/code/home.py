#!/usr/bin/env python3
import os
import subprocess

from time import sleep
import threading

import teamAR as t1
import teamReserva as t2
import partida as pt

def partida():
	pt.run()

def time1():
	t1.run()

def time2():
	t2.run()     

threading.Thread(target=partida).start()
threading.Thread(target=time1).start()
threading.Thread(target=time2).start()

# aguarda tempo da partida
sleep(170)

# --------------------------------------
# var = subprocess.getoutput("ifconfig")
# --------------------------------------