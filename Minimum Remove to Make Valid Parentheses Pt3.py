# Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution(object):

    def stackApproach(self, s):
        stack = []
        removeChar = []
        for i in range(len(s)):
            char = s[i]
            if (char == "("):
                stack.append(i)
            if (char == ")"):
                if (stack):
                    stack.pop()
                else:
                    removeChar.append(i)
        # remove characters at index
        listS = list(s)
        for i in stack + removeChar:
            listS[i] = ""
        return "".join(listS)

    def minRemoveToMakeValid(self, s):
        return self.stackApproach(s)
        """
        :type s: str
        :rtype: str
        """
