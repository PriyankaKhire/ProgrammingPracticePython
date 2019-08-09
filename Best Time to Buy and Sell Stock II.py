#Best Time to Buy and Sell Stock II
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    
    def findPeakValleyPeak(self, prices):
        profit = 0
        valleyIndex = 0
        for i in range(1, len(prices)):
            if(prices[i] < prices[valleyIndex]):
                valleyIndex = i
            else:
                profit = profit + (prices[i] - prices[valleyIndex])
                valleyIndex = i
        return profit
    
    def maxProfit(self, prices):
        return self.findPeakValleyPeak(prices)
        """
        :type prices: List[int]
        :rtype: int
        """
        
