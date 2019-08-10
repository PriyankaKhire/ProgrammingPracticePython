# Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution(object):
    def __init__(self):
        self.maximumProfit = 0
        
    def logic(self, prices, k, index, output, transactionType):
        #  note: adding to output as array so you can see how transactions change
        # I can make output as a number and directly add to it as well.
        print 'the transactions are', output, 'and the profit is', sum(output)
        self.maximumProfit = max(self.maximumProfit, sum(output))
        if(index == len(prices) or k == 0):
            return
        for i in range(index, len(prices)):
            if(transactionType == 'buying'):
                # buy a stock
                print 'buying ', prices[i]
                self.logic(prices, k, i, output+[-prices[i]], 'selling')
            if(transactionType == 'selling'):
                # sell a stock
                print 'selling ', prices[i]
                # after selling you can buy it on the same day
                # after selling a transaction is completed, so we can reduce k
                self.logic(prices, k-1, i, output+[prices[i]], 'buying')            
        
    def maxProfit(self, k, prices):
        self.logic(prices, k, 0, [], 'buying')
        print 'Max profit is ', self.maximumProfit
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
# Main
# Note: you can buy it and sell it on same day too.
obj = Solution()
obj.maxProfit(2, [3,2,6,5,0,3])


