# Majority Element
# https://leetcode.com/problems/majority-element/
class Solution(object):
    def majorityElement(self, nums):
        hashMap = {}
        for element in nums:
            if not(element in hashMap):
                hashMap[element] = 0
            hashMap[element] = hashMap[element] + 1
        return max(hashMap, key=hashMap.get)
        """
        :type nums: List[int]
        :rtype: int
        """
# Main
# Time complexity: O(n)
# Space complexity: O(n)
        
