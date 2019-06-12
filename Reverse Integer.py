#Reverse Integer
#https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        isNegative = False
        #check if its negative
        if(str(x).startswith('-')):
            isNegative = True
            x = int(str(x)[1:])
        #reverse it
        x = int(str(x)[::-1])
        if(isNegative):
            x = -x
        #check if its in range of 32 bit intigers
        if not(x >= -(2**31) and x <= ((2**31)-1) ):
            return 0
        return x
        """
        :type x: int
        :rtype: int
        """

#Main
obj = Solution()
print obj.reverse(1234)
