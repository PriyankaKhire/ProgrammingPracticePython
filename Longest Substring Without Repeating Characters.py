#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Approch1(object):
    def __init__(self, string):
        self.string = string
        self.characterMap = {}
        self.largestWindow = 0

    def insertInCharacterMap(self):
        for letter in self.string:
            if not letter in self.characterMap:
                self.characterMap[letter] = -1

    def existInCurrentWindow(self, windowStart, characterIndex):
        #if character has never been seen before
        if (self.characterMap[self.string[characterIndex]] == -1):
            return False
        if(self.characterMap[self.string[characterIndex]] < windowStart):
            return False
        return True
        

    def solution(self):
        self.insertInCharacterMap()
        windowStart = 0
        windowEnd = 0
        currentIndex = 0
        while currentIndex < len(self.string):
            if(self.existInCurrentWindow(windowStart, currentIndex)):
                #Measure previous window
                print "previous unique character window is "+str((windowEnd - windowStart)+1)
                if (self.largestWindow < ((windowEnd - windowStart)+1)):
                    self.largestWindow = ((windowEnd - windowStart)+1)
                #start new Window
                windowStart = self.characterMap[self.string[currentIndex]]+1
                windowEnd = currentIndex
            else:
                #extendWindow
                windowEnd = currentIndex
            #update hash table
            self.characterMap[self.string[currentIndex]] = currentIndex
            currentIndex = currentIndex +1
        print "previous unique character window is "+str((windowEnd - windowStart)+1)
        if (self.largestWindow < ((windowEnd - windowStart)+1)):
            self.largestWindow = ((windowEnd - windowStart)+1)
        print "Largest window "+str(self.largestWindow)
                 


#Main
o = Approch1("dvdf")
o.solution()
