#Maximum Swap
#Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
#Example 1:
#Input: 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.
#Example 2:
#Input: 9973
#Output: 9973
#Explanation: No swap.
#Note:
#The given number is in the range [0, 108]
class Approch1(object):
    def __init__(self, number):
        self.number = number
        self.zeroToNine = {}
        for i in range(10):
            self.zeroToNine[i] = []
        self.totalNumbers = 0

    #returns true if digits in the given number are in ascending order
    def ifAscending(self, num):
        prev = 0
        while (num >0):
            curr = num%10
            if(curr < prev):
                return False
            num = num/10
            prev = curr
        return True

    def scanNumber(self):
        n = self.number
        pos = 0
        #in number 973 3 is at 0th position and 9 is at 2nd postion
        #so we want higher number at higher position
        while n>0:
            self.zeroToNine[n%10].append(pos)
            pos = pos+1
            n = n/10
        self.totalNumbers = pos

    def solution(self):
        if(self.ifAscending(self.number)):
            return "No swap"
        self.scanNumber()
        print self.totalNumbers
        print self.zeroToNine
        


#Main Program
o = Approch1(9793)
o.solution()
