#Longest Palindromic Substring
#https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):

    def longestPalindromeOfEvenOrOddLength(self, s):
        #modify the string by adding $between every character and then call longestPalindromeOddLength
        new_s = ""
        for char in s:
            new_s = new_s+"$"+char
        new_s = new_s+"$"
        self.longestPalindromeOddLength(new_s)

    def longestPalindromeOddLength(self, s):
        longest_palindrome = ""
        for i in range(1, len(s)):
            print "i is "+str(i)
            j = 1
            while ((i-j)>=0 and (i+j) < len(s) and s[i-j] == s[i+j]):
                j = j+1
            if(j != 1):
                #Palindrome found is between i-j-1 to i+j-1
                temp_palindrome = s[(j-1-i):(i+j)]
                print j
                print j-1-i
                print i+j
                print "temp palindrome is "+temp_palindrome
                if len(temp_palindrome) > len(longest_palindrome):
                    longest_palindrome = temp_palindrome
                    print "longest palindrome now is "+longest_palindrome
        print "longest palindrome of odd length is "+longest_palindrome
            


#Mian Program
o = Solution()
o.longestPalindromeOfEvenOrOddLength("cbbd")
