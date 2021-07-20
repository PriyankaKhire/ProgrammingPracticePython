# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    
    def lengthOfLongestSubstring(self, string):
        if string == "":
            return 0
        hashTable = {}
        windowStart = 0
        windowEnd = 0
        longestLength = 0
        for currentIndex in range(len(string)):
            # if current letter not in hash table
            if (string[currentIndex] not in hashTable):
                hashTable[string[currentIndex]] = currentIndex
                # update the windown end
                windowEnd = currentIndex
                longestLength = max(windowEnd - windowStart+1, longestLength)
            else:
                previousIndex = hashTable[string[currentIndex]]
                # if current letter in hash table
                # it can mean two things
                # 1 current letter is in current windwo, that means we found duplicate
                if (previousIndex >= windowStart and previousIndex <= windowEnd):
                    longestLength = max(windowEnd - windowStart+1, longestLength)
                    # this is the previous index, and we add 1 to it to assign it to new start window.
                    windowStart = previousIndex +1
                    # update the end index and increase the window size.
                    windowEnd = currentIndex
                    # make current index as new postion of this character in hash table
                    hashTable[string[currentIndex]] = currentIndex
                else:
                    # 2 if current letter is not in current window. 
                    hashTable[string[currentIndex]] = currentIndex
                    # update the end index and increase the window size.
                    windowEnd = currentIndex
        # one last time to check the window length.
        longestLength = max(windowEnd - windowStart+1, longestLength)
        return longestLength
        """
        :type s: str
        :rtype: int
        """
        
