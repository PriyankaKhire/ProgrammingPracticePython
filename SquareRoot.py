#Sqrt(x)
#https://leetcode.com/problems/sqrtx/description/
class Approch1(object):
    def sqrt(self, x):
        for i in range(x):
            if(i*i == x):
                return i
            if(i*i > x):
                return i-1
    def mySqrt(self, x):
        print self.sqrt(x)
        """
        :type x: int
        :rtype: int
        """
#based on binary search
class Approch2(object):
    def sqrt(self, x, low, high):
        mid = (low+high)/2
        if(mid*mid == x):
            return mid
        if(((mid*mid) > x) and (((mid-1)*(mid-1)) < x)):
            return mid-1
        if(mid*mid > x):
            return self.sqrt(x, low, mid-1)      
        else:
            return self.sqrt(x, mid+1, high) 
        
    def mySqrt(self, x):
        print self.sqrt(x, 0, x)
        """
        :type x: int
        :rtype: int
        """

#Main
o = Approch1()
o.mySqrt(11)

o1 = Approch2()
o1.mySqrt(2147395599)
