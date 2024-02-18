# Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution(object):

    def characterCount(self, strs):
        # key = character count string, value = [string]
        hashTable = {}
        # for every string, create a character count array
        for s in strs:
            characterArray = [0 for i in range(26)]
            for letter in s:
                # find the index where the letter can go
                index = ord(letter) - ord('a')
                # mark it in array
                characterArray[index] += 1
            # convert the character array into a string
            key = ",".join([str(x) for x in characterArray])
            # add this key to hash table
            if (key not in hashTable):
                hashTable[key] = []
            hashTable[key].append(s)
        output = []
        for key in hashTable:
            output.append(hashTable[key])
        return output

    def sortedApproach(self, strs):
        # key = sorted string, value = [string]
        hashTable = {}
        # put sorted strings in hash along with strings
        for s in strs:
            sortedStr = "".join(sorted(s))  # n log n operation
            if (sortedStr not in hashTable):
                hashTable[sortedStr] = []
            hashTable[sortedStr].append(s)
        output = []
        for key in hashTable:
            output.append(hashTable[key])
        return output

    def groupAnagrams(self, strs):
        # return self.sortedApproach(strs)
        return self.characterCount(strs)
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
