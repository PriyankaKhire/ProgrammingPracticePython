#Group Anagrams
#https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def __init__(self):
        self.hash = {}

    def wordSort(self, word):
        wordToList = list(word)
        wordToList.sort()
        return ''.join(wordToList)
    
    def groupAnagrams(self, strs):
        for word in strs:
            sortedWord = self.wordSort(word)
            if not(sortedWord in self.hash):
                self.hash[sortedWord] = [word]
            else:
                self.hash[sortedWord].append(word)

        output = []
        for key in self.hash:
            output.append( self.hash[key])

        print output
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

#Main Program
o = Solution()
o.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
