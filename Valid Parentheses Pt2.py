# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def switch(self, char):
        hashTable = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        if char in hashTable:
            return hashTable[char]
        return -1
    
    def isValid(self, s):
        stack = []
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stack.append(char)
            else:
                switchValue = self.switch(char)
                if(stack and switchValue != -1 and stack[-1] == switchValue):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """
        
