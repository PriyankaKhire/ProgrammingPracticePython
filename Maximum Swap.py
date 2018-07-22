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
        
class Approch2(object):
    def __init__(self, number):
        self.number = number
        self.power = 0

    def findPower(self):
        for i in range(1,9):
            if not (10**i < self.number):
                break
        self.power = i-1

    def findMax(self, number):
        if number == 0:
            return 0
        maxPos = 0
        maxNum = 0
        pos = 0
        while number >0:
            if(maxNum < (number%10)):
                maxNum = number%10
                maxPos = pos
            number = number/10
            pos = pos+1
        return maxNum, maxPos
                
    def formulateNumber(self, num, power):
        formulatedNumber = num*(10**power)
        for i in range(power):
            formulatedNumber = formulatedNumber + (num*(10**i))
        return formulatedNumber

    def numSwap(self, pos1, pos2):
        stringNum = str(self.number)[::-1]
        t = list(stringNum)
        letter1 = t[pos1]
        letter2 = t[pos2]
        t[pos2] = letter1
        t[pos1] = letter2
        stringNum = ''.join(t)
        stringNum = stringNum[::-1]
        return int(stringNum)
        

    def solution(self):
        self.findPower()
        if(self.power < 1):
            print "No swap"
            return
        number = self.number
        while(self.power >= 1):
            currNum = number/(10**self.power)
            compareNumber = self.formulateNumber(currNum, self.power)
            if(compareNumber < number):
                #find max in remaining numbers and swap
                num, pos = self.findMax(number)
                print "We need to swap "+str(num)+" at postion "+str(pos)+" with number "+str(currNum)+" at position "+str(self.power)
                output = self.numSwap(pos, self.power)
                return output
            number = number%(10**self.power)
            self.power = self.power-1
        return "No swap"
            

#Main Program
o = Approch2(10909091)
print o.solution()
