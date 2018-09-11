#Next Permutation
#https://leetcode.com/problems/next-permutation/description/
class Approch1(object):
    def __init__(self):
        self.output = []
        
    def permutation(self, nums, index):
        if not(nums in self.output):
            self.output.append(list(nums))
        if(index == len(nums)-1):
            return
        for i in range(index+1, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.permutation(nums, index+1)
            nums[i], nums[index] = nums[index], nums[i]
            
    def nextPermutation(self, nums):
        for i in range(len(nums)):
            self.permutation(nums, i)
        #Convert list to number and find such a list that is larger than current nums list
        greaterThanNums = []
        for n in self.output:
            if(int(''.join(str(e) for e in n)) > int(''.join(str(e) for e in nums))):
                greaterThanNums.append(n)
        #finally find the smallest list in our greater than lists
        smallest = 99999999999
        for l in greaterThanNums:
            if(int(''.join(str(e) for e in l)) < smallest):
                smallest = int(''.join(str(e) for e in l))
        print [int(x) for x in str(smallest)]

#Main
o = Approch1()
o.nextPermutation([1,2,3])
