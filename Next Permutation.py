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

class Approch2(object):
    #reverses the numbers from given index to end
    def reverse(self, nums, index):
            totalNumsToReverse = (len(nums)-1)-index
            for i in range(totalNumsToReverse/2):
                nums[index+1+i], nums[(len(nums)-1)-i] = nums[(len(nums)-1)-i], nums[index+1+i]
            return nums
    
    #finds the first number from back that does not follow ascending order
    def findFirstNumNotAscending(self, nums, high):
        for i in range(high, 0, -1):
            if(nums[i-1] < nums[i]):
                return i-1
            
    #finds position of FIRST number that is GREATER than number at given pos    
    def findFirstNumGreaterThanPos(self, pos, nums):
        for i in range(len(nums)-1, pos, -1):
            if(nums[i] > nums[pos]):
                return i
        

    def findNextPrermutation(self, nums, high):
            pos = self.findFirstNumNotAscending(nums, high)
            if (pos == None):
                nums.sort()
                return nums
            greaterNumPos = self.findFirstNumGreaterThanPos(pos, nums)
            #Swap numbers
            nums[pos], nums[greaterNumPos] = nums[greaterNumPos], nums[pos]
            #reverse rest of the numbers
            return self.reverse(nums, pos)
            
    def nextPermutation(self, nums):
        return self.findNextPrermutation(nums, len(nums)-1)

#Main
#o = Approch1()
#o.nextPermutation([1,2,3])

o2 = Approch2()
print o2.nextPermutation([1,2,5,4,3,2,1])

o3 = Approch2()
print o3.nextPermutation([3,2,1])
