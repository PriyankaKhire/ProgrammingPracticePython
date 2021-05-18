# Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution(object):
    
    def createString(self, s, pairIndex):
        string = ""
        for i in range(len(s)):
            if(s[i] == '(' or s[i] == ')'):
                if(i in pairIndex):
                    string = string + s[i]
            else:
                string = string + s[i]
        return string
        
    
    def checkParenthesis(self, s):
        stack = []
        pairIndex = []
        for i in range(len(s)):
            if (s[i] == '('):
                stack.append(i)
            elif(s[i] == ')'):
                if(stack):
                    startIndex = stack.pop()
                    pairIndex.append(startIndex)
                    pairIndex.append(i)
        return pairIndex
        
    def minRemoveToMakeValid(self, s):
        pairIndex = self.checkParenthesis(s)
        return self.createString(s, pairIndex)
        """
        :type s: str
        :rtype: str
        """
        
