# Is Subsequence
# https://leetcode.com/problems/is-subsequence/description

class Solution(object):
    def isSubsequence(self, s, t):
        subStrPtr = 0
        strPtr = 0
        while(subStrPtr < len(s) and strPtr < len(t)):
            if (s[subStrPtr] == t[strPtr]):
                subStrPtr += 1
            strPtr += 1
        if (subStrPtr == len(s)):
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
