#Word break using DP
#https://leetcode.com/problems/word-break/description/

class Solution(object):
    def __init__(self, s, wordDict):
        self.s = s
        self.wordDict = wordDict
        self.matrix = [[0 for col in range(len(s))] for row in range(len(s))]
        #key is start index, and value is end indices.
        self.hashTable = {}

    def fillMatrix(self):
        #There is no need to fill the matrix, but I am doing it for undestanding sake.
        for row in range(len(self.s)):
            for col in range(len(self.s)):
                if(self.s[row:col+1] in self.wordDict):
                    print self.s[row:col+1], row, col
                    self.matrix[row][col] = 1
                    #insert in hash table, where start index is row and end index is col
                    if not(row in self.hashTable):
                        self.hashTable[row] = []
                    self.hashTable[row].append(col)
                    
    def bfsQueueApproch(self):
        if not (0 in self.hashTable):
            return False
        #here we first take 0 and find all its end indices and put it in queue
        q = []
        lastEndIndex = len(self.s)-1
        for index in self.hashTable[0]:
            q.append(index)
        #while queue is not empty pop the first end index and find its next match index in hash table
        while(q):
            topEndIndex = q.pop(0)
            #if we find the end index then we have a match.
            if(topEndIndex == lastEndIndex):
                return True
            #if we find the next index as start index in hash table we add all its end indices in q
            if((topEndIndex+1) in self.hashTable):
                for index in self.hashTable[topEndIndex+1]:
                    q.append(index)
        #if we dont find end index then return false
        return False
                
            
                    
    def logic(self):
        self.fillMatrix()
        print self.hashTable
        print "Can the word "+self.s+" be broken ? ", self.bfsQueueApproch()

#Main
wd = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango", "and"]
obj1 = Solution("ilikesamsungmobile", wd)
obj1.logic()

obj2 = Solution("ilikeicecreamandmango", wd)
obj2.logic()

obj3 = Solution("catsandog" ,["cats", "dog", "sand", "and", "cat"]) 
obj3.logic()

obj3 = Solution("atsanddog" ,["cats", "dog", "sand", "and", "cat"]) 
obj3.logic()
