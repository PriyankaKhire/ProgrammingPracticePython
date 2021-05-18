# Decode Ways
# https://leetcode.com/problems/decode-ways/
class Solution(object):
    
    def isValid(self, number):
        if(number >= 65 and number <= 90):
            return True
        return False
    
    def getChar(self, number):
        return chr(number)
    
    def decode(self, s, index, answer, count):
        if(index == len(s)):
            count[0] = count[0] + 1
            print answer
            return
        for i in range(index, len(s)):
            stringNum = int(s[index:i+1])+64
            if not self.isValid(stringNum):
                return
            character = self.getChar(stringNum)
            self.decode(s, i+1, answer+character, count)     
        
    def numDecodings(self, s):
        count = [0]
        self.decode(s, 0, "", count)
        return count[0]
        """
        :type s: str
        :rtype: int
        """
        
