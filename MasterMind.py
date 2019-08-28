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
class BruteForce(object):
    def __init__(self, master):
        self.master = master
        self.colors = master.colors[:]
        self.numberOfColorsInSequence = len(master.secretSequence)

    def logic(self, seqLen, output):
        if(seqLen == 0):
            print output
            score = self.master.guess(output)            
            if(score == (self.numberOfColorsInSequence,0)):
                print "Correct Guess"
                return True
            return
        for color in self.colors:            
            if(self.logic(seqLen-1, output+[color])):
                return True

    def run(self):
        self.logic(self.numberOfColorsInSequence, [])
        
# Main
m = MasterMind(3, 4)
obj = BruteForce(m)
obj.run()
