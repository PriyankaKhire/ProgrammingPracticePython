#Split Array Largest Sum
#https://leetcode.com/problems/split-array-largest-sum/
#This soluiton is inspired by my split array into m sub arrays approch
#this is a WORST CASE SOLUTION

class Solution(object):

    def findSubArraySum(self, array):
        maxSum = 0
        for subArray in array:
            if(maxSum < sum(subArray)):
                maxSum = sum(subArray)
        print "The max sum of the sub arrays is ", maxSum
    
    def recurrse(self, nums, m, output, index):
        if(len(output) == m):
            if(index < len(nums)):
                print "Since not all nums have been added into the output array we return, output array ", output
            else:
                print "All numbers have been added to output array", output
                self.findSubArraySum(output)
            return
        subArray = []
        for i in range(index, len(nums)):
            subArray.append(nums[i])
            output.append(subArray)
            self.recurrse(nums, m, output, i+1)
            #backtrack by popping subArray from output, but this sub arrya stil has contents added to it
            output.pop()
        
    def splitArray(self, nums, m):
        self.recurrse(nums, m, [], 0)
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
#Main
obj = Solution()
obj.splitArray([7,2,5,10,8], 2)
