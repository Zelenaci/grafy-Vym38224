#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from pylab import pi



class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Funkce cosinus"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Graf")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="ukaž graf", command=self.graf)
        self.btn2.pack()
        
       



    def graf(self):

        index = self.f.curselection()[0]
        self.lines = f.readlines()

        f = open("soubor-ux.txt", "r")
        slovnik = {}
        for line in f:
            slovnik[line.split()[0]] = (line.split()[1:])
        
        print(slovnik)

        t = np.linspace(y,x,z) #Čas
        f = 50                    #Hz
        u = np.cos(2*pi*f*t)      #Napětí
        plt.plot(t,u, c="r", linewidth=2)
        plt.grid()
        plt.ylabel("napětí[V]")
        plt.xlabel("čas[s]")
        plt.title("Cosinus")
        plt.show()






    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()



