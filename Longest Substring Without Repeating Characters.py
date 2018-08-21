#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Approch1(object):
    def __init__(self, string):
        self.string = string
        self.characterMap = {}

    def insertInCharacterMap(self):
        for letter in self.string:
            if not letter in self.characterMap:
                self.characterMap[letter] = -1

    def solution(self):
        self.insertInCharacterMap()
        longestLength = 0
        currLength = 0
        start = 0
        end = 0
        i = 0
        while (i < len(self.string)):
            if self.characterMap[self.string[i]] == -1 :
                print "here", i
                self.characterMap[self.string[i]] = i
                currLength = currLength +1
                if(currLength > longestLength):
                    longestLength = currLength
                    #end = i
            else:
                #start = self.characterMap[self.string[i]]+1
                #end = i
                self.characterMap[self.string[i]] = i
            i = i+1
        print longestLength            


#Main
o = Approch1("pwwkew")
o.solution()
