#word ladder
# https://leetcode.com/problems/word-ladder/description/
class Solution(object):
    
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
        print output
        print endWord
        if(output[-1] == endWord):
            return len(output)
        topWord = output[-1]
        for word in wordList:
            if(word not in output):
                if(self.differentByOne(word, topWord)):
                    self.ladder(output.append(word), endWord, wordList)
            
    
    def ladderLength(self, beginWord, endWord, wordList):
        output = []
        output.append(beginWord)
        print self.ladder(output, endWord, wordList)


#main program
s = Solution()
s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
