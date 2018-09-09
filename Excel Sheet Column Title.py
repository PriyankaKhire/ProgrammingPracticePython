#Excel Sheet Column Title
#https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution(object):
    def recurrse(self, n, string):
        if(n == 0):
            return string
        if(n%26 == 0):
            string = string+'Z'
            return self.recurrse((n/26)-1, string)
        else:
            string = string+chr(ord('A')+(n%26)-1)
            return self.recurrse(n/26, string)
        
    
    def convertToTitle(self, n):
        print self.recurrse(n, "")[::-1]
        """
        :type n: int
        :rtype: str
        """

#Main
o = Solution()
o.convertToTitle(1)
