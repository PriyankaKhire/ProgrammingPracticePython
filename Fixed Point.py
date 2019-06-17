#Fixed Point
#https://leetcode.com/problems/fixed-point/
class Solution(object):
    def fixedPoint(self, A):
        for i in range(len(A)):
            if(A[i] == i):
                return i
        return -1
        """
        :type A: List[int]
        :rtype: int
        """
    
#Main
obj = Solution()
print obj.fixedPoint([-10,-5,0,3,7])
