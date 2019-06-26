#3Sum
#https://leetcode.com/problems/3sum/
#Leetcode time limit excedeed
class HashTableMethod(object):
    def putInHash(self, nums):
        ht = {}
        for i in range(len(nums)):
            if not(nums[i] in ht):
                ht[nums[i]] = [i]
            else:
                ht[nums[i]].append(i)
        return ht

    def is3rdIndex(self, i, j, htKey):
        if(len(htKey)>2):
            return True
        for index in htKey:
            if((index != i) and (index != j)):
                return True
        return False

    def findSum(self, ht, nums):
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tempSum = -nums[i] - nums[j]
                if(tempSum in ht and self.is3rdIndex(i, j, ht[tempSum])):
                    setNum =  sorted([nums[i], nums[j], tempSum])
                    if not(setNum in output):
                        output.append(setNum)
        return output
        
    def threeSum(self, nums):
        ht = self.putInHash(nums)
        print self.findSum(ht, nums)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

class SortMethod(object):

    def twoSum(self, currentSum, startIndex, nums):
        output = []
        endIndex = len(nums)-1
        while(startIndex < endIndex):
            if(nums[startIndex] + nums[endIndex] == currentSum):
                if not([nums[startIndex], nums[endIndex], -currentSum] in output):
                    output.append([nums[startIndex], nums[endIndex], -currentSum])
                startIndex = startIndex + 1
                endIndex = endIndex - 1
            elif(nums[startIndex] + nums[endIndex] > currentSum):
                endIndex = endIndex - 1
            elif(nums[startIndex] + nums[endIndex] < currentSum):
                startIndex = startIndex + 1
        return output

    def logic(self, nums):
        output = []
        for i in range(len(nums)):
            currentNumber = nums[i]
            s = self.twoSum(-currentNumber, i+1, nums)
            if(s != None):
                for sums in s:
                    if not(sums in output):
                        output.append(sums)
        return output
    
    def threeSum(self, nums):
        nums.sort()
        print self.logic(nums)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#Main

obj = HashTableMethod()
obj.threeSum([-1, 0, 1, 2, -1, -4])
obj.threeSum([0,0,0,0])
obj.threeSum([-2,0,1,1,2])

obj = SortMethod()
obj.threeSum([-1, 0, 1, 2, -1, -4])
obj.threeSum([0,0,0,0])
obj.threeSum([-2,0,1,1,2])

