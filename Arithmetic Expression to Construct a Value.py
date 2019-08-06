# Arithmetic Expression to Construct a Value
'''
Given an array nums of positive and negative integers and an int target.
You have +, -, *, / and () operators.
Find out if it's possible to build an expression that evaluates to the target value.
Each operator can only be used once. Return any solution or an empty string if it's not possible.

Example 1:

Input: nums = [1, 2, 3, 8, 4], target = 44
Output: "(3+8)*4"
Example 2:

Input: nums = [2, 3, 4, 1, 9, 2], target = 21
Output: "3+2*9"
'''
class Solution(object):
    def __init__(self):
        # I have not used () just coz I was unclear if a(b) == a*b
        # Also, just in general I thought it was a bit difficult to use brackets.
        self.operators = {'+':1, '-':1, '*':1, '/':1}
        # Reason for using hash: so i don't have to keep track of index numbers.
        self.numHash = {}

    def putInHash(self, nums):
        for num in nums:
            if not(num in self.numHash):
                self.numHash[num] = 1
            else:
                self.numHash[num] = self.numHash[num] + 1

    def evaluate(self, value1, operator, value2):
        if(operator == '+'):
            return value1+value2
        if(operator == '-'):
            return value1-value2
        if(operator == '*'):
            return value1*value2
        if(operator == '/'):
            if(value2 == 0):
                # to avoid divide by zero error
                return 0
            return value1/value2
        

    def backtrack(self, target, expression, value):
        if(target == value):
            print expression
            return True
        for operator in self.operators:
            if(self.operators[operator] > 0):
                for num in self.numHash:
                    if(self.numHash[num] > 0):
                        result = self.evaluate(value, operator, num)
                        if(result > 0 and result <= target):
                            self.operators[operator] = self.operators[operator] - 1
                            self.numHash[num] = self.numHash[num] - 1
                            # Let's add brackets around * and /
                            if(operator == '*' or operator == '/'):
                                flag = self.backtrack(target, "("+expression+")"+operator+str(num), result)
                            else:
                                flag = self.backtrack(target, expression+operator+str(num), result)
                            if(flag):
                                # This return condition prevents function from further backtracking.
                                return True
                            self.operators[operator] = self.operators[operator] + 1
                            self.numHash[num] = self.numHash[num] + 1

    # just returns the first expression that satisfies the condition.
    def getExpression(self, nums, target):
        self.putInHash(nums)
        #Try with every number
        for num in self.numHash:
            self.numHash[num] = self.numHash[num] - 1
            if(self.backtrack(target, str(num), num)):
                return True
            self.numHash[num] = self.numHash[num] + 1


# Main
nums = [1, 2, 3, 8, 4]
target = 44
obj = Solution()
print obj.getExpression(nums,target) # prints (8+3)*4

nums = [2, 3, 4, 1, 9, 2]
target = 21
obj = Solution()
print obj.getExpression(nums,target) # prints (2+9-4)*3
