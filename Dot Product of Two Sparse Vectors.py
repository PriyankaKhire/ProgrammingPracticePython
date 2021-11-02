# Dot Product of Two Sparse Vectors
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector:
    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        if (len(vec.nums) != len(self.nums)):
            return []
        output = 0
        for index in range(len(self.nums)):
            output = output + (self.nums[index] * vec.nums[index])
        return output
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
