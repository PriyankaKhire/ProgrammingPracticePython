# Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        bucket = {}
        # sort all strings alphabetically and add to hash
        for s in strs:
            sortedString = "".join(sorted(s))
            if (sortedString not in bucket):
                bucket[sortedString] = []
            bucket[sortedString].append(s)
        # create list from the bucket hash
        answerList = []
        for sortedString in bucket:
            answerList.append(bucket[sortedString])
        return answerList
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
