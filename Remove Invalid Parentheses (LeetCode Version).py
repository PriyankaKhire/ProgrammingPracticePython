#Remove Invalid Parentheses
#https://leetcode.com/problems/remove-invalid-parentheses/description/

class Solution(object):

    def isValid(self, string):
        stack = []
        for char in string:
            if char == "(":
                stack.append(char)
            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
    
    def dfs(self, s, index, output):
        if index == len(s)-1:
            print output
            return
        
        
    def removeInvalidParentheses(self, s):
        print s

#Main
o = Solution()
o.removeInvalidParentheses("()())()")
print o.isValid("(a)(())()")
