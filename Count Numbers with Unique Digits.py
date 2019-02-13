#Count Numbers with Unique Digits
#https://leetcode.com/problems/count-numbers-with-unique-digits/
class Approch1(object):
    
    def isUnique(self, num):
        if num < 10:
            return True
        hashT = {}
        while num > 0:
            remainder = num%10
            num = num/10
            if remainder in hashT:
                return False
            hashT[remainder] = True
        return True
        
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        count = 0
        for num in range(10**n):
            if (self.isUnique(num)):
                count = count + 1
        return count
        """
        :type n: int
        :rtype: int
        """

#Main
obj1 = Approch1()
print obj1.countNumbersWithUniqueDigits(3)
