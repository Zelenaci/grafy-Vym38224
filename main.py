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
        self.lbl2 = tk.Label(self, text="Nastavení frekvence:")
        self.lbl2.pack()   
        self.f = Entry(self)
        self.f.pack()
        self.f.focus_set()
        def frekvence():
            try:
                f1 = open("frekvence.txt", "w")
            except FileNotFoundError:
                print("Soubor nebyl nalezen")

            text = (self.f.get())
            f1.write(text)
            print(self.f.get())
            f1.close()
        self.btn3 = tk.Button(self, text="zapiš", command=frekvence)
        self.btn3.pack()
        self.btn2 = tk.Button(self, text="ukaž graf", command=self.graf)
        self.btn2.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.hodnoty = []

        
    def graf(self):
        #Čas
        f2 = open("soubor-win.txt", "r")
        radky = f2.readlines()
        x = [float(line.split()[0]) for line in radky]
        self.hodnoty.append(x)
        for radek in self.hodnoty:
                zacatek = radek[0]
                konec = radek[-1]
        x = np.linspace(zacatek, konec,len(radky))
        f2.close      
        #Frekvence
        f1 = open("frekvence.txt", "r")         
        f = f1.read()
        f = np.int16(f)                         
        f1.close()
        #Napětí                           
        u = np.cos(2*pi*f*x)
        #plot     
        plt.plot(x,u, c="r", linewidth=2)
        plt.grid()
        plt.ylabel("napětí[V]")
        plt.xlabel("čas[s]")
        plt.title("Cosinus")
        plt.show()

        
    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()



