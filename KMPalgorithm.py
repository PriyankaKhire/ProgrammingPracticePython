#Knuth-Morris-Pratt algorithm for string matching

class KMP(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    #generate longest suffix which is same as suffix table for a Pattern
    def lps(self):
        table = [0 for i in range(len(self.pattern)+1)]
        i = 1
        j = 2
        
