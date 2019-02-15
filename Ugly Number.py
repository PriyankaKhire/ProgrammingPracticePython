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
class Approch2(object):

    def logic(self, num):
        while num >0:
            if num == 1:
                return True
            if(num%2 == 0):
                num = num/2
            elif(num%3 == 0):
                num = num/3
            elif(num%5 == 0):
                num = num/5
            else:
                break
            
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
print obj1.isUgly(14)

obj2 = Approch2()
print obj2.isUgly(14)
