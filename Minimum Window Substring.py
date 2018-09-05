#Minimum Window Substring
#https://leetcode.com/problems/minimum-window-substring/description/
class Solution(object):
    def __init__(self):
        self.hash = {}
        self.q = []
        self.charCount = 0
        self.windows = []

    def insertInHash(self, t):
        for char in t:
            if not (char in self.hash):
                self.hash[char] = []

    def recordWindow(self, s):
        #print "--------------------------"
        #print "start ", self.q[0]
        #print "end ", self.q[-1]
        #print "hash ", self.hash
        #print "q ", self.q
        #print "character count ", self.charCount
        self.windows.append([self.q[0], self.q[-1]])
        charIndex = self.q.pop(0)
        #print "popped ", charIndex
        #print "queue is ", self.q
        char = s[charIndex]
        self.hash[char].pop(0)
        #print "hash ", self.hash
        if not self.hash[char]:
            self.charCount = self.charCount -1
            #print "character count ", self.charCount
        #print "--------------------------"
    
    def minWindow(self, s, t):
        self.insertInHash(t)
        for i in range(len(s)):
            #print s[i]
            if(s[i] in t):
                if not self.hash[s[i]]:
                    self.charCount = self.charCount+1
                    #print "character count ", self.charCount
                self.hash[s[i]].append(i)
                #print "hash ", self.hash
                self.q.append(i)
                #print "q ", self.q
                while(self.charCount == len(t)):
                    self.recordWindow(s)
        minLength = len(s)
        minWindow = None
        for window in self.windows:
            length = (window[1] - window[0])+1
            if(minLength >= length):
                minLength = length
                minWindow = window
        if minWindow:
            print s[minWindow[0]:minWindow[1]+1]
                

#Main
#o = Solution()
#o.minWindow("ADOBECODEBANC", "ABC")

o = Solution()
o.minWindow("bbaa", "aba")
