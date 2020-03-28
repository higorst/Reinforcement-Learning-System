# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

import constants.constants as constants
from view import Router

def view():  

    def hit():
        info.destroy()
        info.quit()

    # ------------------------------------------------------
    # Definições da view
    info = Tk()
    info.geometry(constants.viewSize)
    info.resizable(0,0)
    info.title(constants.titleTelaInfo)
    info.title(
        constants.titleTelaInfo
    )
    info.configure(
        background=constants.backgroundColorInfo
    )
    scrollbar = Scrollbar(info)
    scrollbar.pack(side=RIGHT, fill=Y)
    # listbox = Listbox(info, yscrollcommand=scrollbar.set)
    # for i in range(1000):
    #     listbox.insert(END, str(i))
    # listbox.pack(side=LEFT, fill=BOTH)

    # scrollbar.config(command=listbox.yview)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Mensagem 00
    # ------------------------------------------------------
    lb = Label(
        info, 
        text=constants.stringInfo00, 
        bg=constants.backgroundColorInfo,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaInfo
        )
    )
    lb.place(
        x=20, 
        y=constants.yLenghtLabelMessage * 1,
        anchor=W
    )
    # ------------------------------------------------------
    # Mensagem 01
    # ------------------------------------------------------
    lb = Label(
        info, 
        text=constants.stringInfo01, 
        bg=constants.backgroundColorInfo,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaInfo
        )
    )
    lb.place(
        x=20, 
        y=constants.yLenghtLabelMessage * 2,
        anchor=W
    )
    # ------------------------------------------------------
    # Mensagem 02
    # ------------------------------------------------------
    lb = Label(
        info, 
        text=constants.stringInfo02, 
        bg=constants.backgroundColorInfo,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaInfo
        )
    )
    lb.place(
        x=20, 
        y=constants.yLenghtLabelMessage * 3,
        anchor=W
    )
    # ------------------------------------------------------
    # Mensagem 03
    # ------------------------------------------------------
    lb = Label(
        info, 
        text=constants.stringInfo03, 
        bg=constants.backgroundColorInfo,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaInfo
        )
    )
    lb.place(
        x=20, 
        y=constants.yLenghtLabelMessage * 4,
        anchor=W
    )
    # ------------------------------------------------------
    # Mensagem 04
    # ------------------------------------------------------
    lb = Label(
        info, 
        text=constants.stringInfo04, 
        bg=constants.backgroundColorInfo,
        fg=constants.letterColor
    )
    lb.config(
        font=(
            constants.fontPersonalizada, 
            constants.fontSizeTitleTelaInfo
        )
    )
    lb.place(
        x=20, 
        y=constants.yLenghtLabelMessage * 5,
        anchor=W
    )
    # ------------------------------------------------------


    # ------------------------------------------------------
    # Img 01
    # ------------------------------------------------------
    width = int(454 / constants.proportionInfoImage)
    height = int(314 / constants.proportionInfoImage)
    img = Image.open(constants.addressInfo01)
    img = img.resize((width,height), Image.ANTIALIAS)
    img01 = ImageTk.PhotoImage(img)
    panel = Label(info, image=img01, bg=constants.backgroundColorInfo)
    panel.place(x=450, y=5, anchor=N)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Img 02
    # ------------------------------------------------------
    width = int(457 / constants.proportionInfoImage)
    height = int(315 / constants.proportionInfoImage)
    img = Image.open(constants.addressInfo02)
    img = img.resize((width,height), Image.ANTIALIAS)
    img02 = ImageTk.PhotoImage(img)
    panel = Label(info, image=img02, bg=constants.backgroundColorInfo)
    panel.place(x=750, y=300, anchor=E)
    # ------------------------------------------------------

    # ------------------------------------------------------
    # Img 03
    # ------------------------------------------------------
    width = int(450 / constants.proportionInfoImage)
    height = int(317 / constants.proportionInfoImage)
    img = Image.open(constants.addressInfo03)
    img = img.resize((width,height), Image.ANTIALIAS)
    img03 = ImageTk.PhotoImage(img)
    panel = Label(info, image=img03, bg=constants.backgroundColorInfo)
    panel.place(x=450, y=595, anchor=S)
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        info, 
        width=8, 
        text=constants.titleButtonInfoMessage,
        bg=constants.butonColor, 
        fg=constants.letterColor,
        activebackground=constants.activeButtonColorInfo
    )
    bt.place(
        x=115, 
        y=constants.yLenghtLabelMessage * 5, 
        anchor=W
    )
    # ------------------------------------------------------

    # ------------------------------------------------------
    bt = Button(
        info, 
        width=5, 
        text=constants.btInfoBack, 
        command=hit,
        bg=constants.butonColorInfo, 
        fg=constants.letterColor,
        bd=1,
        activebackground=constants.activeButtonColorInfo
    )
    bt.config(highlightbackground=constants.borderColorButtonInfo)
    bt.place(
        x=780, 
        y=595, 
        anchor=SE
    )
    # ------------------------------------------------------

    info.mainloop()

if __name__ == '__main__':
    view()