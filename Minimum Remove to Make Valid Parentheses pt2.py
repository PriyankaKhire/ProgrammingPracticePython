# Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution(object):
    def stringBuilder (self, s, removeParenthesis):
        string = ""
        for i in range(len(s)):
            if (i not in removeParenthesis):
                string = string + s[i]
        return string
        
    def stackApproach(self, s):
        extraParenthesis = []
        stack = []
        for i in range(len(s)):
            if (s[i] == "("):
                stack.append(i)
            if (s[i] == ")"):
                if not stack:
                    extraParenthesis.append(i)
                else:
                    stack.pop()
        return stack+extraParenthesis
            
    def minRemoveToMakeValid(self, s):
        removeParenthesis = self.stackApproach(s)
        return self.stringBuilder(s, removeParenthesis)
        """
        :type s: str
        :rtype: str
        """
        
