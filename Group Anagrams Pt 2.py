# Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def __init__(self):
        self.hashMap = {}
    
    def sortString(self, string):
        stringList = sorted(string)
        return ''.join(stringList)
    
    def addToMap(self, strs):
        for string in strs:
            sortedString = self.sortString(string)
            if (sortedString not in self.hashMap):
                self.hashMap[sortedString] = []
            self.hashMap[sortedString].append(string)
    
    def listSortedStrings(self):
        sortedStringList = []
        for key in self.hashMap:
            sortedStringList.append(self.hashMap[key])
        return sortedStringList
            
    def groupAnagrams(self, strs):
        self.addToMap(strs)
        return  self.listSortedStrings()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
