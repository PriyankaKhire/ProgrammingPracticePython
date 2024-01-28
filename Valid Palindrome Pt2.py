# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution(object):
    def convertString(self, s):
        newStr = ""
        for char in s:
            if (char.isalnum()):
                newStr += char
        return newStr.lower()
    
    def palindromeCheck(self, s):
        start = 0
        end = len(s)-1
        while (start < end):
            if (s[start] != s[end]):
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome(self, s):
        # Get rid of all non-alphanumeric characters and convert it into lower case
        newStr = self.convertString(s)
        # Check if the new string is palindrome or not
        return self.palindromeCheck(newStr)
        """
        :type s: str
        :rtype: bool
        """
        
