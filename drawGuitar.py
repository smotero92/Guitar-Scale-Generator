from graphics import *


def drawGuitar(scale, rotate,showNotes):
    notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    center = 50

    win = GraphWin("Co5", 1200, 400)

#create note list for all strings in a standard tuning guitar
    a5String = [x for x in range(0,12)]
    a5 = a5String + a5String
    e1String = a5String[7::] + a5String[0:7] + a5String[7::] + a5String[0:7]
    b2String = a5String[2::] + a5String[0:2] + a5String[2::] + a5String[0:2]
    g3String = a5String[10::] + a5String[0:10] + a5String[10::] + a5String[0:10]
    d4String = a5String[5::] + a5String[0:5] + a5String[5::] + a5String[0:5]
    e6String = e1String[:] + e1String[:]
    strings = [e6String, a5, d4String, g3String, b2String, e1String]
    stringNames = ["E6", "A5", "D4", "G3", "B2", "E1"]
    guitarSize = 18
    stringsDrawn = [x for x in range(0,6)]
    notesDrawn = [x for x in range(0,17)]
    notesCircles = [x for x in range(0,19)]

    #draw the strings of the guitar
    for x in  range(0,len(stringsDrawn)):
        stringsDrawn[5-x] = Line(Point(50,100+40*x),Point(1100,100+40*x))
        stringsDrawn[5-x].draw(win)
    #Draw the frets
    for x in range(0,guitarSize):
        line = Line(Point(50+50*x,100),Point(50+50*x,300))
        line.draw(win)
        #draw all fret numbers but not the open strings
        fretNum = Text(Point(25+50*x, 340), str(x))
        fretNum.setSize(13)
        if x > 0 :
            fretNum.draw(win)
        for y in range(0, 6):
            if (strings[y][x] in scale):
                noteDrawP = Point(75+50*(x-1),300-40*y)
                notesCircles[x] = Circle(noteDrawP,20)
                #initialize the notes text, draw it after deciding what color it is
                noteText = Text(noteDrawP, notes[strings[y][x]])
                noteText.setSize(9)
                noteText.setTextColor("red")
                #Draw the circles to show the frets on the strings that are included in the specified scale
                #If the current note being drawn is the root, color it green
                if strings[y][x] == scale[0]:
                    notesCircles[x].setFill("green")
                    noteText.setTextColor("#dd3eff")
                else:
                    notesCircles[x].setFill("#b9ecff")
                    noteText.setTextColor("ffccb9")
                notesCircles[x].draw(win)
                if showNotes == 1 and x>0:
                    noteText = Text(noteDrawP, notes[strings[y][x]])
                    noteText.setSize(8)
                    noteText.draw(win)
        #draw the names of the strings (open notes)
        if x < len(stringsDrawn):
            stringText = Text(Point(29, 100+40*x),stringNames[5-x])
            stringText.setSize(13)
            stringText.draw(win)

    win.getMouse()
    win.close()
