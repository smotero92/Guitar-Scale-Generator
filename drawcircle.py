from graphics import *
import math


def drawCircle(scale, rotate):
    notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    pi = math.pi

    center = 250
    win = GraphWin("Co5", center*2, center*2)


    base = Circle(Point(center, center), 150)
    base.draw(win)

    notesDrawn = [x for x in range(0,12)]
    notesCircles = [x for x in range(0,12)]

    for x in range(0,12):
        if x in scale:
            notesCircles[x] = Circle(Point(185*math.sin((-1*x*pi/6+pi/2))+center,185*math.cos(-1*x*pi/6+pi/2)+center),37)
            if x == scale[0]:
                notesCircles[x].setFill("green")
            else:
                notesCircles[x].setFill("blue")
            notesCircles[x].draw(win)

        notesDrawn[x] = Text(Point(185*math.sin((-1*x*pi/6+pi/2))+center,185*math.cos(-1*x*pi/6+pi/2)+center),notes[x])
        notesDrawn[x].setSize(14)
        notesDrawn[x].draw(win)


    win.getMouse()
    win.close()
