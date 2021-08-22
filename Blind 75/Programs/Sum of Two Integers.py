# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

class Solution(object):
    
    # These adders don't work for negative numbers
    def halfSubtractor(self, a, b):
        # XOR for subtraction 
        currDifference = a^b
        # compliment any 1 number and AND for carry, refer to truth table.
        carry = ~a&b
        return currDifference, carry
    
    # These adders don't work for negative numbers
    def halfAdder(self, a, b):
        # XOR for the sum
        currSum = a^b
        # AND for the carry
        carry = a&b
        return currSum, carry
    
    # Only works when abs(a) > abs(b), here we perform a-b
    def subtraction(self, a, b):
        # get current sum and carry
        currAnswer, carry = self.halfSubtractor(a, b)
        
        while carry > 0:
            # Left Shift the carry
            carry = carry << 1
            # Add the carry and sum
            currAnswer, carry = self.halfSubtractor(currAnswer, carry)
        
        return currAnswer
    
    # Only works when both are positive, here we perform a+b
    def addition(self, a, b):
        # get current sum and carry
        currAnswer, carry = self.halfAdder(a, b)
        
        while carry > 0:
            # Left Shift the carry
            carry = carry << 1
            # Add the carry and sum
            currAnswer, carry = self.halfAdder(currAnswer, carry)
        
        return currAnswer
    
    
    def getSum(self, a, b):
        # If one of them is zero
        if (a == 0):
            return b
        if (b == 0):
            return a
        # If both are positive
        if (a > 0 and b > 0):
            return self.addition(a, b)
        # If both are negarive
        if (a < 0 and b < 0):
            answer = self.addition(abs(a), abs(b))
            return -answer
        # If one of them is negative
        # if abs(a) == abs(b)
        if (abs(a) == abs(b)):
            return 0
        # if abs(a) > abs(b)
        if (abs(a) > abs(b)):
            # if b is negative a-b
            if (b < 0):
                return self.subtraction(abs(a), abs(b))
            # if a is negative
            if (a < 0):
                answer = self.subtraction(abs(a), abs(b))
                return -answer
        # if abs(b) > abs(a)
        if (abs(b) > abs(a)):
            # if a is negative b-a
            if (a < 0):
                return self.subtraction(abs(b), abs(a))
            # if b is negative
            if (b < 0):
                answer = self.subtraction(abs(b), abs(a))
                return -answer
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
