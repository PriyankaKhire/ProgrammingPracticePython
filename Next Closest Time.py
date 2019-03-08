#Next Closest Time
#https://leetcode.com/problems/next-closest-time/

class Solution(object):
    def __init__(self):
        self.numbers = []

    def sortNumbers(self, time):
        for char in time:
            if(char != ":"):
                self.numbers.append(int(char))
        self.numbers.sort()

    def findNextGreatTime(self, time):
        return ""

    def findGreaterNumber(self, lastNumber):
        for number in self.numbers:
            if(number > lastNumber):
                return number, True
        return -1, False

    def logic(self,time):
        self.sortNumbers(time)
        lastNumber = int(time[-1])
        #now there are 2 cases with last number
        #1) if we find the a nubmer in sorted numbers to be greater than current last number in time
        greaterNumber, flag = self.findGreaterNumber(lastNumber)
        if(flag):
            return time[:4]+str(greaterNumber)+time[5:]
        else:
            return self.
            
        
    def nextClosestTime(self, time):
        print self.logic(time)
        """
        :type time: str
        :rtype: str
        """
#Main
obj = Solution()
obj.nextClosestTime("19:39")
