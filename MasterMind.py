import random
class MasterMind(object):
    def __init__(self, numberOfColors, numberOfColorsInSequence):
        # Here your colors are assigned numbers instead of name
        self.colors = [color for color in range(numberOfColors)]
        self.secretSequence = [random.choice(self.colors) for i in range(numberOfColorsInSequence)]
        print "The secret is",self.secretSequence

    def guess(self, g):
        # copy secret sequence, as you see below we are modifying the secret sequence, and we dont want to do it to original secret.
        sequence = self.secretSequence[:]
        if(len(g) != len(sequence)):
            print "Please make a guess of length",len(sequence)
            return
        numberOfColorsInSamePlaceAndSameColor = 0        
        for i in range(len(g)):
            if(g[i] == sequence[i]):
                numberOfColorsInSamePlaceAndSameColor = numberOfColorsInSamePlaceAndSameColor + 1
                # since we have counted that color we mark it.
                g[i] = 'x'
                sequence[i] = 'x'        
        numberOfColorsInDifferentPlaceButSameColor = 0
        for i in range(len(g)):
            if(g[i] != 'x' and g[i] in sequence):
                numberOfColorsInDifferentPlaceButSameColor = numberOfColorsInDifferentPlaceButSameColor + 1
                # since we have counted that color instance we mark it.
                sequence[sequence.index(g[i])] = 'x'
        return numberOfColorsInSamePlaceAndSameColor, numberOfColorsInDifferentPlaceButSameColor

# Here I don't make use of the numberOfColorsInSamePlaceAndSameColor and numberOfColorsInDifferentPlaceButSameColor.
# I just mindlessly generate all possible combinations of colors and match it and see if I can get a match.
# Worst case guesses exponential
class BruteForce(object):
    def __init__(self, master):
        self.master = master
        self.colors = master.colors[:]
        self.numberOfColorsInSequence = len(master.secretSequence)
        self.attemptNumber = 0

    def logic(self, seqLen, output):
        if(seqLen == 0):
            print output
            score = self.master.guess(output)
            self.attemptNumber = self.attemptNumber + 1
            if(score == (self.numberOfColorsInSequence,0)):
                print "Correct Guess made in",self.attemptNumber,"attempts"
                return True
            return
        for color in self.colors:            
            if(self.logic(seqLen-1, output+[color])):
                return True

    def run(self):
        self.logic(self.numberOfColorsInSequence, [])

# Lets try to use numberOfColorsInSamePlaceAndSameColor variable.
# This solution works best if total number of colors is very large and number of colors in sequence is very small.
# we eleminate the colors that are not present in secert.
# ok so this improves the average case a LOT, but the worst case still remains the same.
class Improvement1(object):
    def __init__(self, master):
        self.master = master
        self.colors = master.colors[:]
        self.numberOfColorsInSequence = len(master.secretSequence)
        self.attemptNumber = 0

    def findColorsInSequence(self):
        colorsInSequence = []
        for color in self.colors:
            score = self.master.guess([color for i in range(self.numberOfColorsInSequence)])
            if(score[0] > 0):
                colorsInSequence.append(color)
        print "The colors present in secret sequence are",colorsInSequence
        return colorsInSequence

    def allCombinationsOfColorsInSeq(self, colorsInSequence, seqLen, output):
        if(seqLen == 0):
            print output
            score = self.master.guess(output)
            self.attemptNumber = self.attemptNumber + 1
            if(score == (self.numberOfColorsInSequence,0)):
                print "Correct Guess made in",self.attemptNumber,"attempts"
                return True
            return
        for color in colorsInSequence:
            if(self.allCombinationsOfColorsInSeq(colorsInSequence, seqLen-1, output+[color])):
                return True

    def run(self):
        colorsInSequence = self.findColorsInSequence()
        self.allCombinationsOfColorsInSeq(colorsInSequence, self.numberOfColorsInSequence, [])

# Here I make use of dummy color -> 'd'
class Improvement2(object):
    def __init__(self, master):
        self.master = master
        self.colors = master.colors[:]
        self.numberOfColorsInSequence = len(master.secretSequence)
        self.guessSeq = ['d' for i in range(self.numberOfColorsInSequence)]

    def findPosOfColor(self):
        for color in self.colors:
            score = self.master.guess([color for i in range(self.numberOfColorsInSequence)])
            if(score[0] > 0):
                print "Color",color,"present in sequence in",score[0],"positions"

    def run(self):
        self.findPosOfColor()
# Main
m = MasterMind(3, 4)
#brute = BruteForce(m)
#brute.run()
#print "First improvement"
#imp1 = Improvement1(m)
#imp1.run()
imp2 = Improvement2(m)
imp2.run()
