# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# Solution understood from.
# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/358879/Java-Solution-Explained-and-Easy-to-Understand-for-Interviews
'''
formula: (length of substring - number of times of the maximum occurring character in the substring) <= k
'''
class Solution(object):
    def addToHashMap(self, letter, hashMap):
        if (letter not in hashMap):
            hashMap[letter] = 0
        hashMap[letter] = hashMap[letter] + 1
        #print hashMap
    
    def characterReplacement(self, s, k):
        # key: character; value: count
        hashMap = {}
        start = 0
        maxOccurringCharCount = 0
        longestLength = 0
        for end in range(len(s)):
            #print "start", start, "end", end
            #print "longestLength", longestLength
            self.addToHashMap(s[end], hashMap)
            # if the current letter is most frequently occurring then update the count.
            maxOccurringCharCount = max(maxOccurringCharCount, hashMap[s[end]])
            # get the length of current substring
            substringLength = (end - start)+1
            if((substringLength - maxOccurringCharCount) <= k):
                longestLength = max(longestLength, substringLength)
            else:
                # since the character at start is no longer in our window
                hashMap[s[start]] = hashMap[s[start]] - 1
                start = start + 1
        return longestLength
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
