#Intersection of Two Arrays
#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution(object):
    def putInHash(self, nums):
        ht = {}
        for num in nums:
            if not(num in ht):
                ht[num] = True
        return ht
    def intersection(self, nums1, nums2):
        ht = self.putInHash(nums1)
        output = []
        for num in nums2:
            if(num in ht):
                if not(num in output):
                    output.append(num)
        return output
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
