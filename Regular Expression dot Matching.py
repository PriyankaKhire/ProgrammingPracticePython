# Regular Expression . Matching
# https://leetcode.com/problems/regular-expression-matching/
# '.' Matches any single character.
class Solution(object):
    def recurse(self, s, p):
        # if pattern is over and string is not
        if(len(p) == 0 and len(s) > 0):
            return
        if(s == p):
            return True
        # 1) if p[0] == .
        if(len(s) > 0 and (p[0] == "." or p[0] == s[0])):
            s = s[1:]
            p = p[1:]
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
obj.isMatch("aa", ".")

obj = Solution()
obj.isMatch("a", ".")

obj = Solution()
obj.isMatch("", ".")
