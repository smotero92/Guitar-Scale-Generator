import drawcircle
import buildscale
import drawGuitar

from Tkinter import *
from tkFileDialog import askopenfilename


class buildMenu(Frame):



    scale = buildscale.Scale()

    def createWidgets(self):

        def makeAndDrawCO5(rt,sig,mode,rot):
            drawcircle.drawCircle(self.scale.buildScale(rt,sig,mode), rot)


        def makeAndDrawGuitar(rt,sig,mode,rot, showNotes):
            drawGuitar.drawGuitar(self.scale.buildScale(rt,sig,mode), rot, showNotes)

        def buildCo5(event):
            makeAndDrawCO5(self.rootEntry.get(), self.sigEntry.get(), int(self.modeEntry.get()), int(self.rotEntry.get()))
        def buildGuitarWNotes(event):
            makeAndDrawGuitar(self.rootEntry.get(), self.sigEntry.get(), int(self.modeEntry.get()), int(self.rotEntry.get()),1)
        def buildGuitarWoNotes(event):
            makeAndDrawGuitar(self.rootEntry.get(), self.sigEntry.get(), int(self.modeEntry.get()), int(self.rotEntry.get()),0)

        def quit(event):
            import sys; sys.exit()

        self.rootEntry = Spinbox(self,values = sorted(self.scale.rootTrans.keys()),wrap= True)
        self.rootEntry.grid(row = 0, column = 0)

        self.sigEntry = Spinbox(self, values = self.scale.sigTrans.keys(), wrap= True)
        self.sigEntry.grid(row = 0, column = 1)

        self.modeEntry = Spinbox(self,from_= 1, to = 10)
        self.modeEntry.grid(row = 0, column = 2)

        self.rotEntry = Spinbox(self,from_= 0, to = 11)
        self.rotEntry.grid(row = 0, column = 3)

        self.buildCo5 = Button(self, text = "Show Co5")
        self.buildCo5.bind('<Button-1>', buildCo5)
        self.buildCo5.grid(row = 1, column = 0)

        self.build = Button(self, text = "Show Guitar w/ Notes")
        self.build.bind('<Button-1>', buildGuitarWNotes)
        self.build.grid(row = 1, column = 1)

        self.build = Button(self, text = "Show Guitar w/o Notes")
        self.build.bind('<Button-1>', buildGuitarWoNotes)
        self.build.grid(row = 1, column = 2)


        self.gtfo = Button(self, text = "quit")
        self.gtfo.bind('<Button-1>', quit)
        self.gtfo.grid(row = 1, column = 3)


    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        self.scale = buildscale.Scale()


root = Tk()
buildAScale = buildMenu(master=root)
buildAScale.mainloop()
root.destroy()
