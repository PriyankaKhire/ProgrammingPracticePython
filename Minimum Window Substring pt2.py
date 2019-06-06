#Minimum Window Substring
#https://leetcode.com/problems/minimum-window-substring/
class Solution(object):
    def __init__(self):
        self.counter = None
        self.window = None
        self.letterIndexQueue = []
        self.hashTable = {}

    def putInHash(self, t):
        for char in t:
            if not(char in self.hashTable):
                self.hashTable[char] = [1, []]
            else:
                self.hashTable[char][0] = self.hashTable[char][0] + 1
        print self.hashTable

    def logic(self, s):
        index = 0
        while(index < len(s)):
            print "current letter ", s[index], " at index ", index
            if(s[index] in self.hashTable):
                print "Current letter in hash table"
                self.hashTable[s[index]][0] = self.hashTable[s[index]][0] - 1
                print "hash table status of current letter ", self.hashTable[s[index]]
                if(self.hashTable[s[index]][0] >= 0 ):
                    self.counter = self.counter - 1
                print "The counter now is ", self.counter
                self.hashTable[s[index]][1].append(index)
                print "the hash table status now becomes ", self.hashTable[s[index]]
                self.letterIndexQueue.append(s[index])
                print "the letter index queue is ", self.letterIndexQueue
            index = index + 1
            while(self.counter == 0):
                startWindowLetter = self.letterIndexQueue[0]
                endWindowLetter = self.letterIndexQueue[-1]
                print "Window Starts from ", self.hashTable[startWindowLetter][1][0],
                print "Window ends at ", self.hashTable[endWindowLetter][1][0]
                print "window Size is ", (self.hashTable[endWindowLetter][1][0] - self.hashTable[startWindowLetter][1][0] + 1)
                if(len(self.window) > (self.hashTable[endWindowLetter][1][0] - self.hashTable[startWindowLetter][1][0] + 1)):
                    self.window = s[self.hashTable[startWindowLetter][1][0]:self.hashTable[endWindowLetter][1][0]+1]
                self.letterIndexQueue.pop(0)
                print "After popping the letter index queue now becomes ", self.letterIndexQueue
                self.hashTable[startWindowLetter][1].pop(0)
                self.hashTable[startWindowLetter][0] = self.hashTable[startWindowLetter][0] + 1
                print "The hash table status of start letter ",startWindowLetter, self.hashTable[startWindowLetter]
                if(self.hashTable[startWindowLetter][0] > 0):
                    self.counter = self.counter + 1
                print "The counter now is ", self.counter
                if(self.letterIndexQueue):
                    index = self.hashTable[endWindowLetter][1][0]+1
                print "index now is at ", index
            print self.hashTable, self.counter
                
        
    def minWindow(self, s, t):
        if(s == t):
            return t
        self.counter = len(t)
        self.window = s
        self.putInHash(t)
        self.logic(s)
        print "The minimum window substring is ", self.window
        """
        :type s: str
        :type t: str
        :rtype: str
        """
#Main
obj = Solution()
obj.minWindow('ADOBECODEBANC', 'ABC')

obj = Solution()
#obj.minWindow('a', 'aa')
