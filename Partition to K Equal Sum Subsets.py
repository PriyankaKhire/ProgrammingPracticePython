#Partition to K Equal Sum Subsets
#https://www.geeksforgeeks.org/check-if-it-possible-to-partition-in-k-subarrays-with-equal-sum/
#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
class Solution(object):
    def __init__(self):
        self.hash = {}

    def putInHash(self, nums):
        for element in nums:
            if not(element in self.hash):
                self.hash[element] = 1
            else:
                self.hash[element] = self.hash[element] + 1
        print self.hash

    def getSets(self, k, proposedSum, currentSet, totalElements):
        print currentSet, "Total elements",totalElements, "Proposed sum",proposedSum
        if(len(currentSet) >= k and totalElements == 0):
            if(len(currentSet) == k):
                return True
            return
        # start new set if previous set's sum is equal to proposed sum
        if(sum(currentSet[-1]) == proposedSum):
            currentSet.append([])
        for key in self.hash:
            if(self.hash[key] > 0 and sum(currentSet[-1])+key <= proposedSum):
                currentSet[-1].append(key)
                self.hash[key] = self.hash[key] - 1
                print "Printing current set", currentSet[-1]
                if(self.getSets(k, proposedSum, currentSet, totalElements-1)):
                    return True
                print "Printing backtracking current set", currentSet[-1]
                self.hash[key] = self.hash[key] + 1
                #taking back newly created set
                if not(currentSet[-1]):
                    currentSet.pop()
                currentSet[-1].pop()

    def ifSetsExists(self, nums, k, proposedSum):
        currentSet = [[]]
        self.getSets(k, proposedSum, currentSet, len(nums))
        if (currentSet == [[]]):
            return False
        return True
            
    def canPartitionKSubsets(self, nums, k):
        # first we sum the whole array and see if it's divisible by k, coz if it ain't then we cannot divide it in K parts
        if(sum(nums)%k  != 0):
            return False
        # then we see what should the sum be for each sub set, it is worth noting that we are dividing the array in SubSETS and NOT SubARRAY
        proposedSum = sum(nums)/k
        print proposedSum
        # We are just supposed to return true or false for IF the array can be divided, we don't have to return sub sets
        self.putInHash(nums)
        # now check if we can build the set or not
        print self.ifSetsExists(nums, k, proposedSum)
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

#Main
obj = Solution()
obj.canPartitionKSubsets([1, 4, 2, 3, 5 ], 3)

obj = Solution()
obj.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)

obj = Solution()
obj.canPartitionKSubsets([2,2,2,2,3,4,5], 4)

obj = Solution()
obj.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3)

