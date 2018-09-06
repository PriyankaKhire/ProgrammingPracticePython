#Subsets
#https://leetcode.com/problems/subsets/description/
class Solution(object):
    
    def dfs(self, nums, index, output):
        print output
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            output.append(nums[i])
            self.dfs(nums, i+1, output)
            #backtrack
            output.pop()        

    def subsets(self, nums):
        self.dfs(nums, 0, [])
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#Main
o = Solution()
o.subsets([1,2,3])
