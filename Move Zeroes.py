#Move Zeroes
#https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        firstZero = 0
        while(firstZero < len(nums)):
            if (nums[firstZero] == 0):
                #find first number after 0
                firstNum = firstZero+1
                while(firstNum < len(nums) and nums[firstNum] == 0):
                    firstNum = firstNum+1
                if (firstNum < len(nums)):
                    nums[firstZero] = nums[firstNum]
                    nums[firstNum] = 0
            firstZero = firstZero+1
        print nums


#Main
o = Solution()
o.moveZeroes([0,1,0,3,12])
