#Sum of Two Integers
#https://leetcode.com/problems/sum-of-two-integers/
class Solution(object):
    def halfAdderWithShift(self, xor, carry):
        print xor, carry
        if(carry == 0):
            return xor
        #shift carry by 1 place
        carry = carry << 1
        #With this new carry we do (xor, and) again
        return self.halfAdderWithShift(xor^carry, xor&carry)
        
    def getSum(self, a, b):
        print self.halfAdderWithShift(a^b, a&b)
        """
        :type a: int
        :type b: int
        :rtype: int
        """
#Main
obj = Solution()
obj.getSum(6,2)
print "We remember half adder logic, that truth table resembles xor ^, and &"
print "This solution does not work for negative numbers"
