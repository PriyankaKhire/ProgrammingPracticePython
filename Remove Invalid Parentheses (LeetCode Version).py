#Remove Invalid Parentheses
#https://leetcode.com/problems/remove-invalid-parentheses/description/

class Solution(object):
    def __init__(self):
        self.output = []

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
        if index == len(s):
            if(self.isValid(output)):
                self.output.append(output)
            return
        for i in range(index, len(s)):
            self.dfs(s, i+1, output+s[i])
        
    def removeInvalidParentheses(self, s):
        self.dfs(s, 0, "")
        maxLength = 0
        #find max length in outputs
        for o in self.output:
            if(len(o) > maxLength):
                maxLength = len(o)
        #remove min length solutions
        sol = []
        for o in self.output:
            if(len(o) == maxLength and not(o in sol)):
                sol.append(o)
        print sol

#Main
o = Solution()
o.removeInvalidParentheses("(a)())()")

