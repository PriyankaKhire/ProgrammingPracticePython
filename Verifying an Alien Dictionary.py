# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution(object):
    def __init__(self):
        self.orderHash = {}
        
    def putOrderInHash(self, order):
        for i in range(len(order)):
            self.orderHash[order[i]] = i
    
    def compareWords(self, w1, w2):
        i = 0
        j = 0
        while(i<len(w1) and j<len(w2)):
            print w1[i], w2[j]
            if(w1[i] == w2[j]):
                i = i+1
                j = j+1
            else:
                if(self.orderHash[w1[i]] > self.orderHash[w2[j]]):
                    return False
                return True
        # Case where first word is larger than second like apple vs app. we want app before apple
        if(i < len(w1)):
            return False
        return True
            
    def isAlienSorted(self, words, order):
        self.putOrderInHash(order)
        for i in range(len(words)-1):
            if not(self.compareWords(words[i], words[i+1])):
                return False
        return True
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
