# Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# took hints from
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39665/Java-solution-with-just-two-traverses.
class Solution(object):

    def findMaxStockPricesOnRight(self, prices):
        maxStockPricesOnRight = [0 for i in range(len(prices))]
        # fill the last stock price
        maxStockPricesOnRight[len(prices)-1] = prices[len(prices)-1]
        for i in range(len(prices)-2, -1, -1):
            maxStockPricesOnRight[i] = max(maxStockPricesOnRight[i+1], prices[i])
        return maxStockPricesOnRight

    def findMinStockPricesOnLeft(self, prices):
        minStockPricesOnLeft = [float("inf") for i in range(len(prices))]
        # fill the first stock price
        minStockPricesOnLeft[0] = prices[0]
        for i in range(1, len(prices)):
            minStockPricesOnLeft[i] = min(minStockPricesOnLeft[i-1], prices[i])
        return minStockPricesOnLeft

    def getProfitOnLeft(self, prices, minStockPricesOnLeft):
        profitOnLeft = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            # its either the previous profit made or current stock price- min stock price found on left
            profitOnLeft[i] = max(profitOnLeft[i-1], abs(prices[i]-minStockPricesOnLeft[i]))
        return profitOnLeft

    def getProfitOnRight(self, prices, maxStockPricesOnRight):
        profitOnRight = [0 for i in range(len(prices))]
        for i in range(len(prices)-2, -1, -1):
            # its either the previous profit made or current stock price - max stock price on right
            profitOnRight[i] = max(profitOnRight[i+1], abs(prices[i]-maxStockPricesOnRight[i]))
        return profitOnRight
    
    def maxProfit(self, prices):
        minStockPricesOnLeft = self.findMinStockPricesOnLeft(prices)
        maxStockPricesOnRight = self.findMaxStockPricesOnRight(prices)
        profitOnLeft = self.getProfitOnLeft(prices, minStockPricesOnLeft)
        profitOnRight = self.getProfitOnRight(prices, maxStockPricesOnRight)
        # find the max profit of 2 transactions
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, profitOnLeft[i]+profitOnRight[i])
        print profit
        """
        :type prices: List[int]
        :rtype: int
        """
# Main
obj = Solution()
obj.maxProfit([7, 1, 5, 3, 6, 4])

obj = Solution()
obj.maxProfit([3,3,5,0,0,3,1,4])

obj = Solution()
obj.maxProfit([1,2,3,4,5])

obj = Solution()
obj.maxProfit([7,6,4,3,1])
