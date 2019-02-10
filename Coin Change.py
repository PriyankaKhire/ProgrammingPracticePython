#Coin Change
#https://leetcode.com/problems/coin-change/
class Approch1(object):
    def __init__(self, coins, amount):
        self.coins = coins
        self.amount = amount
        self.totalCoins = [0 for row in range(amount+1)]

    def fillMatrix(self):
        #fill 1s where amount = coin amount
        #so when amount is 1 and coin has value 1 we fill 1 there in that respective row and col
        for coinIndex in range(len(self.coins)):
            if(self.amount >= self.coins[coinIndex]):
                self.totalCoins[self.coins[coinIndex]] = 1
        #fill the rest of the rows
        for row in range(self.amount+1):
            print "Current row amount is ", row
            #if we already have min coins for the amount
            if(self.totalCoins[row] > 0):
                print "\n"
                continue
            #Start looking up
            totalCoins = 999999999
            for prevRow in range(row-1, 0, -1):
                print "Previous row amount is ", prevRow
                #there are 2 things that can happen
                #1) the previous row amount is the multiple of current row amound
                #2) the previous row is not a multiple in that case we need to find remainder amount.
                #in either cases we need to find the min amount.
                #first find number if coins previous row has and is greater than 0
                if(self.totalCoins[prevRow] > 0):
                    #if previous row is multiple of the current row
                    if(row%prevRow == 0):
                        print "previous row amount is a multiple of current row amount"
                        if(totalCoins > (row/prevRow) * self.totalCoins[prevRow]):
                            totalCoins = (row/prevRow) * self.totalCoins[prevRow]
                            print "total coins collected with multiple is ", totalCoins
                    #then if remainder coins row has coins greater than zero
                    if(self.totalCoins[row-prevRow] > 0):
                        if(totalCoins > (self.totalCoins[prevRow]+self.totalCoins[row-prevRow])):
                            totalCoins = self.totalCoins[prevRow]+self.totalCoins[row-prevRow]
                            print "total coins collected with remainder is ", totalCoins
            if(totalCoins != 999999999):
                self.totalCoins[row] = totalCoins
            print "\n"                

    def logic(self):
        self.fillMatrix()
        print "The given coins are ", self.totalCoins
        print "The total coins for amount ", self.amount, " is ", self.totalCoins[-1]
#Main
obj1 = Approch1([1,2,5], 11)
obj1.logic()

obj2 = Approch1([2], 3)
obj2.logic()

obj3 = Approch1([1], 1)
obj3.logic()

obj4 = Approch1([1], 0)
obj4.logic()
