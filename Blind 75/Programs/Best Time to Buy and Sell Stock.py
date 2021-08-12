# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        lowestSoFar = float('inf')
        maxProfit = 0
        for price in prices:
            if (price < lowestSoFar):
                lowestSoFar = price
            maxProfit = max(maxProfit, (price-lowestSoFar))
        return maxProfit
        """
        :type prices: List[int]
        :rtype: int
        """
        
