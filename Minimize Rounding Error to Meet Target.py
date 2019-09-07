# Minimize Rounding Error to Meet Target
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/
import math
class Backtracking(object):
    def findRoundingError(self, list1, list2):
        error = 0
        for i in range(len(list1)):
            error = error + abs(list1[i] - float(list2[i]))
        return error
        
    def logic(self, prices, index, output, target, smallestRoundingError):
        if(index == len(prices)):
            if(sum(output) == target):
                print output
                roundingError = self.findRoundingError(output, prices)
                print roundingError
                smallestRoundingError[0] = min(roundingError, smallestRoundingError[0])
            return 
        # floor
        self.logic(prices, index+1, output+[math.floor(float(prices[index]))], target, smallestRoundingError)
        # ceil
        self.logic(prices, index+1, output+[math.ceil(float(prices[index]))], target, smallestRoundingError)
        
    def minimizeError(self, prices, target):
        smallestRoundingError = [float("inf")]
        self.logic(prices, 0, [], target, smallestRoundingError)
        if(smallestRoundingError[0] != float("inf")):
            print "The smallest rounding error is",smallestRoundingError[0]
        else:
            print -1
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
# Main
obj = Backtracking()
obj.minimizeError(["0.700","2.800","4.900"], 8)

obj.minimizeError(["1.500","2.500","3.500"], 10)
