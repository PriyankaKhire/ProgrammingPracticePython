#Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
class LetterInfo(object):
    def __init__(self):
        self.indegree = 0
        self.lettersAfterMe = []
        
class Solution(object):
    def __init__(self):
        self.alphabets = {}

    def putInHash(self, words):
        for word in words:
            for char in word:
                if not(char in self.alphabets):
                    self.alphabets[char] = LetterInfo()

    def findLetterInfo(self, words):
        for i in range(len(words)-1):
            #print words[i], words[i+1]
            # find the first mismatch letter
            letterIndex = 0
            while(letterIndex < min(len(words[i]), len(words[i+1]))):
                if(words[i][letterIndex] != words[i+1][letterIndex]):
                    #print words[i][letterIndex], words[i+1][letterIndex]
                    # add i+1 word's letter as letters that come after me for word i's letter
                    self.alphabets[words[i][letterIndex]].lettersAfterMe.append(words[i+1][letterIndex])
                    # increase i+1 letter's indegree
                    self.alphabets[words[i+1][letterIndex]].indegree = self.alphabets[words[i+1][letterIndex]].indegree + 1
                    # break coz per word max we can only find one letter pair.
                    break
                letterIndex = letterIndex + 1
        for obj in self.alphabets:
            print obj, self.alphabets[obj].lettersAfterMe, self.alphabets[obj].indegree

    def bfs(self):
        queue = []
        # put all letters with indegree 0 in queue
        for letter in self.alphabets:
            if(self.alphabets[letter].indegree == 0):
                queue.append(letter)
        # there is a cycle if non of the letters have indegree as 0.
        if not queue:
            return ""
        result = []
        while(queue):
            top = queue.pop(0)
            if not(top in result):
                result.append(top)
            # reduce the indegree, this helps if there is case like a->b, c->b
            #self.alphabets[top].indegree = self.alphabets[top].indegree - 1
            queue.extend(self.alphabets[top].lettersAfterMe)
        return "".join(result)
                    
        
    def alienOrder(self, words):
        print words
        self.putInHash(words)
        self.findLetterInfo(words)
        print self.bfs()
        """
        :type words: List[str]
        :rtype: str
        """
# Main
obj = Solution()
#obj.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])

obj = Solution()
#obj.alienOrder(["z", "x"])

obj = Solution()
#obj.alienOrder(["z", "x", "z"])

obj = Solution()
#obj.alienOrder(["ac","ab","b"])

obj = Solution()
obj.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"])
