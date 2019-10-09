# Regular Expression * Matching
# https://leetcode.com/problems/regular-expression-matching/
# Here we are only gonna match the * operator.
# the condition to match a * is that it matches 0 or more of the preeceeding element
class Solution(object):
    def recurse(self, s, p):
        # ther is a special case where s = "" and p = "*" and this is false
        if(s == "" and p == "*"):
            return
        # pattern is over but stirng is not so its false
        if(len(p) == 0 and len(s) > 0):
            return
        if(s == p):
            return True
        # there are 2 cases
        # 1) if first char is * then preeceeding char is nothing
        if(p[0] == "*"):
            # delete first char
            p = p[1:]
            return self.recurse(s, p)
        # 2) if second char is *
        if(len(p) > 1 and p[1] == "*"):
            # i) if first char of string matches p[0]
            if(len(s) > 0 and s[0] == p[0]):
                s = s[1:]
                return self.recurse(s, p)
            # ii) if first char of string does not match p[0]
            elif(len(s) == 0 or s[0] != p[0]):
                p = p[2:]
                return self.recurse(s, p)
            
    def isMatch(self, s, p):
        print self.recurse(s, p)
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
# Main
obj = Solution()
obj.isMatch("mississippi", "mis*is*p*i")

obj = Solution()
obj.isMatch("aab", "c*a*b")

obj = Solution()
obj.isMatch("aa", "a*")

obj = Solution()
obj.isMatch("", "*")

obj = Solution()
obj.isMatch("", "a*")
