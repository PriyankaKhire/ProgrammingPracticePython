#Unique Binary Search Trees
#https://leetcode.com/problems/unique-binary-search-trees/description/
class Solution(object):
    def __init__(self):
        self.dp = []

    #the logic here is let us imagine:
    #n = 2 for numbers 1, 2 => when root is 1 it only has 2 on right side and when 2 is root it only has 1 on left side.
    # thus we can have dp[1]+dp[1] = 1+1 = 2
    #n = 4 for numbers 1,2,3,4 => when 1 is root it has 2,3,4 on right side, when 2 is root it has 1 on left and 3,4 on right side
    # when 3 is root it has 1,2 on left side and 4 on right side and when 4 is root it has 1,2,3 on left side
    #thus it is dp[3]+(dp[1]*dp[2])+(dp[2]*dp[1])+dp[3] = 5+(1*2)+(2*1)+5 = 14
    #thus the formula becomes:
    # (dp[n-1]*dp[0]+dp[n-2]*dp[1]+...+(dp[n/2]*dp[n/2 -1]))*2
    def evenN(self,n):
        halfTotal = 0
        for i in range(n/2):
            halfTotal = halfTotal + (self.dp[i] * self.dp[n-i-1])
        self.dp[n] = 2*halfTotal

    #similarly the formula for odd n is
    #dp[n-1]*dp[0] + dp[n-2]*dp[1] ... dp[n+1 /2]*dp[n+1 / 2 - 1]
    #dont get too confused its same as even n but just add dp[n-1/2]*dp[n-1/2]
    #if you get too confused by this just see tushar roy's explanation
    def oddN(self,n):
        halfTotal = 0
        for i in range((n-1)/2):
            halfTotal = halfTotal + (self.dp[i]*self.dp[n-i-1])
        self.dp[n] = (2*halfTotal)+(self.dp[(n-1)/2]*self.dp[(n-1)/2])
        
        
    def numTrees(self, n):
        if n == 0 or n==1:
            return 1
        self.dp = [0 for i in range(n+1)]
        self.dp[0] = 1
        self.dp[1] = 1
        for i in range(2, n+1):
            if(i%2 == 0):
                self.evenN(i)
            else:
                self.oddN(i)
        return self.dp
        
        """
        :type n: int
        :rtype: int
        """
#Main
obj = Solution()
print obj.numTrees(6)
