#Valid Palindrome II
#https://leetcode.com/problems/valid-palindrome-ii/description/
class Base(object):
    def palindrome(self, s):
        for i in range((len(s))/2):
            if(s[i] != s[(len(s)-1)-i]):
                return False
        return True
    
class Approch1(Base):
    def validPalindrome(self, s):
        if(self.palindrome(s)):
            return True
        
        for i in range(len(s)):
            if(self.palindrome(s[:i] + s[i + 1:])):
                return True
        return False
        """
        :type s: str
        :rtype: bool
        """
class Approch2(Base):
    def validPalindrome(self, s):
        if(self.palindrome(s)):
            return True
        
        for i in range((len(s))/2):
            if(s[i] != s[(len(s)-1)-i]):
                #remove character at first ith index and see if it's a palindrome
                if(self.palindrome(s[:i] + s[i + 1:])):
                    return True
                if(self.palindrome(s[:((len(s)-1)-i)] + s[((len(s)-1)-i) + 1:])):
                    return True
                return False
#Main
o = Approch2()
print o.validPalindrome("aba")
