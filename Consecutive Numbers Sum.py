# Consecutive Numbers Sum
#https://leetcode.com/problems/consecutive-numbers-sum/
class Solution(object):
    def logic(self, N):
        consequitiveNumberCount = 0
        windowStart = 1
        windowEnd = 2
        window = windowStart + windowEnd
        while(windowEnd < N and windowStart < N):
            while(window < N):
                windowEnd = windowEnd + 1
                window = window + windowEnd
                if(window == N):
                    consequitiveNumberCount = consequitiveNumberCount + 1                    
            window = window - windowStart
            windowStart = windowStart + 1
            if(window == N):
                consequitiveNumberCount = consequitiveNumberCount + 1
        print consequitiveNumberCount
                            
                
    def consecutiveNumbersSum(self, N):
        if(N==1 or N==2):
            return 1
        if(N==3):
            return 2
        self.logic(N)
        """
        :type N: int
        :rtype: int
        """
#Main
obj = Solution()
obj.consecutiveNumbersSum(5)
