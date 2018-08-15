#Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Approch1(object):
    def __init__(self, prices):
        self.prices = prices
        self.min = prices[0]
        self.profit = 0

    def maxProfit(self):
        if not self.prices:
            return 0
        for stockPrice in self.prices:
            if(stockPrice < self.min):
                self.min = stockPrice
            else:
                profit = stockPrice - self.min
                if(profit > self.profit):
                    self.profit = profit
        print self.profit

#Main
o = Approch1([7,1,5,3,6,4])
o.maxProfit()
