#Ugly Number II
#https://leetcode.com/problems/ugly-number-ii/
class Approch1(object):
    def __init__(self):
        #filled values for number 0 and 1
        self.uglyNumbers = [False, True]

    #returns true if the prime factors are 2,3,5
    def primeFactors(self, num):
        #print num
        if(num == 2 or num == 3 or num == 5):
            return True
        primeFactors = [2,3,5]
        for factor in primeFactors:
            #print "Factor ", factor, "remainder",num/factor, "hash value ",self.uglyNumbers[num/factor] 
            if(num%factor == 0 and self.uglyNumbers[num/factor] == True):
                return True
        return False

    def nthUglyNumber(self, n):
        count = 1
        num = 1
        while(count < n):
            num = num+1
            if(self.primeFactors(num)):
                count = count+1
                self.uglyNumbers.append(True)
            else:
                self.uglyNumbers.append(False)
        print num
        """
        :type n: int
        :rtype: int
        """

#Main
obj1 = Approch1()
obj1.nthUglyNumber(11)
