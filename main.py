#!/usr/bin/env python3

import pylab as pl
import tkinter as tk

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *



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
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.focus_set()
        def frekvence():
            try:
                f1 = open("frekvence.txt", "w")
            except FileNotFoundError:
                print("Soubor nebyl nalezen")

            text = (self.entry.get())
            f1.write(text)
            print(self.entry.get())
            f1.close()
        self.btn3 = tk.Button(self, text="zapiš", command=frekvence)
        self.btn3.pack()
        self.btn2 = tk.Button(self, text="ukaž graf", command=self.grafsoubor)
        self.btn2.pack() 
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def quit(self, event=None):
        super().quit()
        

        
    def grafsoubor(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while 1:
            radek = f.readline()
            if radek =="":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        pl.figure()
        pl.plot(x,y)
        pl.grid(True)
        pl.show()
        
        
        
        



    def graf(self):
        #Frekvence
        f1 = open("frekvence.txt", "r")         
        f = f1.read()
        f = np.int16(f)                         
        f1.close()
        #Napětí                           
        #u = np.cos(2*pi*f*x)
        #plot     
        #plt.plot(x,u, c="r", linewidth=2)
       #plt.grid()
        plt.ylabel("napětí[V]")
        plt.xlabel("čas[s]")
        plt.title("Cosinus")
        #plt.show()

        
app = Application()
app.mainloop()



