# Count All Valid Pickup and Delivery Options
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
class Solution(object):
    def __init__(self):
        self.count = 0
        
    def generateOrders(self, pickup, delivery, visitedP, visitedD, combination):
        if(len(combination) == 2*len(pickup)):
            print combination
            self.count = self.count+1
            return
        
        for j in range(len(delivery)):
            # if we have picked up but not delivered the jth order.
            if(visitedP[j] == True and visitedD[j] == False):
                visitedD[j] = True
                self.generateOrders(pickup, delivery, visitedP, visitedD, combination+[delivery[j]])
                visitedD[j] = False
                
        for i in range(len(pickup)):
            # pickup the ith order.
            if (visitedP[i] == False):
                visitedP[i] = True
                self.generateOrders(pickup, delivery, visitedP, visitedD, combination+[pickup[i]])
                visitedP[i] = False
                
    def countOrders(self, n):
        pickup = ['p'+str(i+1) for i in range(n)]
        delivery = ['d'+str(j+1) for j in range(n)]
        self.generateOrders(pickup, delivery, [False for i in range(n)], [False for j in range(n)], [])
        return self.count
        """
        :type n: int
        :rtype: int
        """
        
