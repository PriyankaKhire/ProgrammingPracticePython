# Jewels and Stones
#https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, J, S):
        if(J == "" or S == ""):
            return 0
        ht = {}
        for char in J:
            ht[char] = True
        count = 0
        for char in S:
            if (char in ht):
                count = count +1
        print count 
        """
        :type J: str
        :type S: str
        :rtype: int
        """
#Main
obj = Solution()
obj.numJewelsInStones("aA", "aAAbbbb")
