"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import BOTH
import tkinter as tk
from tkinter.ttk import Frame
from PIL import Image , ImageTk

WIDTH = 250
HEIGHT = 150
X0 = 300;
Y0=300

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Simple")
        self.centerWindow()

    def centerWindow(self):

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - WIDTH)/2
        y = (sh - HEIGHT)/2
        self.master.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))

        img = ImageTk.PhotoImage(Image.open('resources/captures/TEST1_1.png'))

        panel = tk.Label(image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        self.img_panel = panel
        # self.pack(fill=BOTH, expand=1)


def main():

    root = tk.Tk()
    # root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, X0, Y0))
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()