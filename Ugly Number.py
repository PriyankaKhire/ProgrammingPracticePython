#Ugly Number
#https://leetcode.com/problems/ugly-number/

class Approch1(object):

    def logic(self, num):
        if(num == 1):
            return True
        if(num%2 == 0 and self.logic(num/2)):
            return True
        if(num%3 == 0 and self.logic(num/3)):
            return True
        if(num%5 == 0 and self.logic(num/5)):
            return True
        
    def isUgly(self, num):
        if self.logic(num):
            return True
        return False
        """
        :type num: int
        :rtype: bool
        """

#Main
obj1 = Approch1()
obj1.isUgly(8)
