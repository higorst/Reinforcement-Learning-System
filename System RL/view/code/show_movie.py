#!/usr/bin/env python3
import os
import subprocess
from time import sleep
from sys import exit
import threading

def run(name, t):

	def show():
		input_ = 'cd && vlc --no-video-title-show --no-repeat  ' + name
		os.system(input_)

	threading.Thread(target=show).start()