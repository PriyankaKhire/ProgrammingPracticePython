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

    def replaceString(self, time, index, string):
        return time[:index]+string+time[index+1:]

    def findGreaterNumber(self, lastNumber):
        for number in self.numbers:
            if(number > lastNumber):
                return number, True
        return -1, False

    def logic(self,time):
        self.sortNumbers(time)
        #now there are few cases with last number
        #1) if we find the a nubmer in sorted numbers to be greater than current last number in time
        greaterNumber, flag = self.findGreaterNumber(int(time[-1]))
        if(flag):
            return self.replaceString(time, 4, str(greaterNumber))
        #2) if we find a number in sorted number to be greater than current second last number in time
        secondGreaterNumber, flag = self.findGreaterNumber(int(time[-2]))
        if(flag and secondGreaterNumber < 6):
            time = self.replaceString(time, 3, str(secondGreaterNumber))
            return self.replaceString(time, 4, str(self.numbers[0]))
        #3) if we find a number in sorted numbers to be greater than current third last number in time
        thirdLastNumber, flag = self.findGreaterNumber(int(time[-4]))
        if(flag and int(time[0]+str(thirdLastNumber)) < 24 ):
            time = self.replaceString(time, 1, str(thirdLastNumber))
            time = self.replaceString(time, 3, str(self.numbers[0]))
            return self.replaceString(time, 4, str(self.numbers[0]))
        #4)else replace everything with the smallest number
        time = self.replaceString(time, 0, str(self.numbers[0]))
        time = self.replaceString(time, 1, str(self.numbers[0]))
        time = self.replaceString(time, 3, str(self.numbers[0]))
        return self.replaceString(time, 4, str(self.numbers[0]))
        
    def nextClosestTime(self, time):
        print self.logic(time)
        """
        :type time: str
        :rtype: str
        """
#Main
obj = Solution()
obj.nextClosestTime("23:59")
