# Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
    def getFinalString(self, string):
        stack = []
        for char in string:
            if(char == '#'):
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack
        
    def backspaceCompare(self, S, T):
        return self.getFinalString(S) == self.getFinalString(T)
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

# Main
obj = Solution()
print obj.backspaceCompare("ab#c", "ab#c")

obj = Solution()
print obj.backspaceCompare("a#c", "b")
