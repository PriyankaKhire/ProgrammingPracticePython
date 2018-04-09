#word ladder
# https://leetcode.com/problems/word-ladder/description/
class Solution(object):

    def __init__(self):
        self.sol = None
    
    #Returns true if 2 words differ by 1 letter
    def differentByOne(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if(w1[i] != w2[i]):
                count = count +1
                if(count > 1):
                    return False
        if(count == 1):
            return True
        return False
    
    def ladder(self, output, endWord, wordList):
        if(output[-1] == endWord):
            #print str(len(output))
            #print output
            if( not self.sol):
                self.sol=len(output)
            if((self.sol) > len(output)):
                self.sol = len(output)
            return 
        topWord = output[-1]
        for word in wordList:
            if(word not in output):
                if(self.differentByOne(word, topWord)):
                    output.append(word)
                    self.ladder(output, endWord, wordList)
                    #Backtrack
                    output.pop()
            
    
    def ladderLength(self, beginWord, endWord, wordList):
        output = []
        output.append(beginWord)
        self.ladder(output, endWord, wordList)
        return self.sol


#main program
s = Solution()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
