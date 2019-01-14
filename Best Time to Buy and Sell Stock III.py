#Best Time to Buy and Sell Stock III
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Backtrack(object):
    def __init__(self, array):
        self.array = array

    def recurrse(self, index, output):
        if(len(output) == 2):
            print "Buy on day ", output[0][0], " sell on day ", output[0][1]," with profit of ", (self.array[output[0][1]]-self.array[output[0][0]]),
            print " and buy on day ", output[1][0]," sell on day ", output[1][1], " with profit of ",(self.array[output[1][1]]-self.array[output[1][0]])
            print "Total profit = ",((self.array[output[0][1]]-self.array[output[0][0]])+(self.array[output[1][1]]-self.array[output[1][0]]))
            return
        for i in range(index+1, len(self.array)):
            if(self.array[i] > self.array[index]):
                output.append([index, i])
                self.recurrse(i+1, output)
                output.pop()

    def logic(self):
        for i in range(len(self.array)):
            self.recurrse(i, [])
            
 
    

#Main
a1 = [3,3,5,0,0,3,1,4]
obj1 = Backtrack(a1)
obj1.logic()

print "\n"

obj2 = Backtrack([1,2,3,4,5])
obj2.logic()

obj3 = Backtrack([7,6,4,3,1])
obj3.logic()
