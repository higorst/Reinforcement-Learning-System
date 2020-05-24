# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import threading

import constants.constants as constants

def closePopup(popupRoot):
	# Finaliza popup
	popupRoot.destroy()
	popupRoot.quit()

def show(s, t):
	popupRoot = Tk()
	popupRoot.wm_attributes('-type', 'splash')
	popupRoot.title(constants.titlePopup)
	popupRoot.configure(
	    background=constants.backgroundColorPopup
	)
	popupRoot.after(t, lambda getTeam=closePopup: closePopup(popupRoot))
	Label(
	    popupRoot, 
	    text='',
	    bg=constants.backgroundColorPopup
	).pack()
	Label(
	    popupRoot, 
	    text=s,
	    bg=constants.backgroundColorPopup,
	    font=(
                constants.fontPersonalizada
            )
	).pack()
	windowWidth = popupRoot.winfo_reqwidth()
	windowHeight = popupRoot.winfo_reqheight()
	positionRight = int(popupRoot.winfo_screenwidth()/2 - windowWidth/2)
	positionDown = 60
	# positionDown = int(popupRoot.winfo_screenheight()/2 - windowHeight/2)
	popupRoot.geometry(constants.sizePopup + "+{}+{}".format(positionRight-100, positionDown))
	# popupRoot.geometry(constants.sizePopup)
	popupRoot.mainloop()


def run(s, t = 3500):
	threading.Thread(target=lambda show=show: show(s, t)).start()