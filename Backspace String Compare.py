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
class LeetcodeSuggested(object):
    def getFinalString(self, string):
        skipCount = 0
        stng = ""
        for char in reversed(string):
            if(char == '#'):
                skipCount = skipCount+1
            else:
                if(skipCount > 0):
                    skipCount = skipCount -1
                else:
                    stng = stng + char
        return stng[::-1]

    def backspaceCompare(self, S, T):
        return self.getFinalString(S) == self.getFinalString(T) 

# Main
obj = Solution()
obj = LeetcodeSuggested()
print obj.backspaceCompare("ab#c", "ab#c")

obj = Solution()
obj = LeetcodeSuggested()
print obj.backspaceCompare("a#c", "b")
