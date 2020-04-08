# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants

def closePopup(popupRoot):
	# Finaliza popup
	popupRoot.destroy()
	popupRoot.quit()


def run(s, t = 3500):
	popupRoot = Tk()
	popupRoot.title(constants.titlePopup)
	popupRoot.configure(
	    background=constants.backgroundColor
	)
	popupRoot.after(t, lambda getTeam=closePopup: closePopup(popupRoot))
	Label(
	    popupRoot, 
	    text='',
	    bg=constants.backgroundColor
	).pack()
	Label(
	    popupRoot, 
	    text=s,
	    bg=constants.backgroundColor
	).pack()
	popupRoot.geometry(constants.sizePopup)
	popupRoot.mainloop()