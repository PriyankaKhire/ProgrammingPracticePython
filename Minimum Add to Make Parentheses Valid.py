# Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
    def minAddToMakeValid(self, s):
        if (s == ""):
            return 0
        openBrackets = 0
        closedBrakets = 0
        for char in s:
            if (char == "("):
                openBrackets = openBrackets + 1
            else:
                if (openBrackets > 0):
                    openBrackets = openBrackets - 1
                else:
                    closedBrakets = closedBrakets + 1
        return openBrackets + closedBrakets
        """
        :type s: str
        :rtype: int
        """
        
