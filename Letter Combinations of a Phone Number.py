#Letter Combinations of a Phone Number
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution(object):
    def __init__(self):
        self.hash = { "0":[" "], "1": ["*"], "2":["a","b","c"], "3": ['d','e','f'], "4":['g','h','i'], "5":['j','k','l'], "6":['m','n','o'], "7":['p','q','r','s'], "8":['t','u','v'], "9":['w','x','y','z']}
        self.output = []

    def permutation(self,digitIndex, string, digits):
        if(digitIndex == len(digits)):
            self.output.append(string)
            return
        for char in self.hash[digits[digitIndex]]:
            self.permutation(digitIndex+1, string+char, digits)

                    
    def letterCombinations(self, digits):
        if not digits:
            return []
        for char in self.hash[digits[0]]:
            self.permutation(1, char, digits)
        print self.output
        """
        :type digits: str
        :rtype: List[str]
        """

#Main
o = Solution()
o.letterCombinations("23")
