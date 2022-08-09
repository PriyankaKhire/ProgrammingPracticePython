# Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution(object):
    def dupRemove(self, s, k):
        ws = 0
        we = 0
        newStr = ''
        while (ws < len(s) and we < len(s)):
            #print "ws", ws, "we", we
            if (ws == we):
                we += 1
                continue
            while(we < len(s) and s[ws] == s[we] and len(s[ws:we]) < k):
                we += 1
            if (len(s[ws:we]) == k):
                # remove string between indeces s[ws:we]
                s = s[:ws]+s[we:]
                # adjust end index because we removed characters from s
                we -= k
            ws = we
        return s
    
    def iterative(self, originalS, k):
        # remove duplicates
        newS = self.dupRemove(originalS, k)
        while(newS != originalS):
            #print originalS, newS
            originalS = newS
            newS = self.dupRemove(originalS, k)
        return newS
                
        
    def removeDuplicates(self, s, k):
        return self.iterative(s, k)
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
