# Plus One
# https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        newNumber = []
        remainder = 1
        for i in range(len(digits)-1, -1, -1):
            addedNumber = digits[i] + remainder
            tempNumber = addedNumber%10
            remainder = addedNumber/10
            newNumber.insert(0, tempNumber)
        if (remainder > 0):
            newNumber.insert(0, remainder)
        return newNumber
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
