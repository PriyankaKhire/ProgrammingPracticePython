# Palindrome Number
# https://leetcode.com/submissions/detail/1108452218/

class Solution(object):
    def checkForPalindrome(self, string):
        for i in range(len(string)):
            if(string[i] != string[len(string)-1-i]):
                return False
        return True

    def createString(self, num, string):
        if (num == 0):
            return
        string[0] += str(num%10)
        self.createString(num/10, string)

    def isPalindrome(self, x):
        if (x < 0):
            return False
        string = [""]
        self.createString(x, string)
        return self.checkForPalindrome(string[0])
        """
        :type x: int
        :rtype: bool
        """
