#Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if(char == "(" or char == "{" or char == "["):
                stack.append(char)
            else:
                if(stack and ((char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{"))):
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        return True
        """
        :type s: str
        :rtype: bool
        """

#Main
obj = Solution()
print obj.isValid("(){{}}{[]}")
