class Scale(object):

    #Input of the root and key signature will be strings, then converted to
    #integer/array format for handling


    def __init__(self):




        """self.rootTrans = {
        "A" : 0,
        "A#/Bb" : 1, "A#" : 1, "Bb" : 1,
        "B" : 2,
        "C" : 3,
        "C#/Db": 4, "C#" : 4, "Db" : 4,
        "D" : 5,
        "D#/Eb":6, "D#" : 6, "Eb" : 6,
        "E" : 7,
        "F" : 8,
        "F#/Gb": 9, "F#" : 9, "Gb" : 9,
        "G" : 10,
        "G#/Ab": 11, "G#" : 11, "Ab" : 11
        }"""
        self.rootTrans = {
        "A" : 0,
        "A#/Bb" : 1,
        "B" : 2,
        "C" : 3,
        "C#/Db": 4,
        "D" : 5,
        "D#/Eb":6,
        "E" : 7,
        "F" : 8,
        "F#/Gb": 9,
        "G" : 10,
        "G#/Ab": 11,
        }

        self.sigTrans = {
        "Major" : [0,2,4,5,7,9,11],
        "Natural Minor" : [0,2,3,5,7,8,10],
        "Harmonic Minor" : [0,2,3,5,7,8,11],
        "Melodic Minor" : [0,2,3,5,7,9,11],
        "Pentatonic Major" : [0,2,4,7,9],
        "Pentatonic Minor" : [0,3,5,7,10],
        "Blues" : [0,3,5,6,7,10],
        "Dorian" : [0,2,3,5,7,9,10],
        "Full" : [x for x in range(0,12)],
        "Hungarian Gypsy" : [0, 2, 3, 6, 7, 8, 11]
        }




    def buildScale(self, rootIn, signatureIn, mode):
        self.roots = self.rootTrans[rootIn]
        self.sig = self.sigTrans[signatureIn]

        self.notesBase = list(range(0,12))
        self.notesTransposed = self.notesBase[self.roots::]+self.notesBase[0:self.roots]
        self.scale = [self.notesTransposed[x] for x in self.sig]
        if mode > 1:
            self.scaleReturn = self.scale[(mode-1)::] + self.scale[0:(mode-1)]
        else:
            self.scaleReturn = self.scale

        return self.scaleReturn

#aMajor = Scale()
