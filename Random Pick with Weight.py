# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
# this problem is same as the one you got on facebook onsite.
import random
class Solution(object):

    def __init__(self, w):
        self.totalWeight = sum(w)
        # assign indices on number line
        self.hashTable = {i:[] for i in range(len(w))}
        # first index in value of hash table represents start point of number line
        # second index represents end point of number line.
        # so for numbers [1,2,2]
        # if the number line is [0, 1, 2, 3, 4]
        # then the indices according to their weights are [0, 1, 1, 2, 2]
        # which means since weight of index 0 is 1 we give it 1 space on number line
        # since weight of index 1 is 2 we give it 2 spaces on number line.
        # so in hash table we represent it 0: 0,0  1:1,2  2: 3,4
        self.hashTable[0] = [0, 0+w[0]-1]
        for i in range(1, len(w)):
            start = self.hashTable[i-1][1]+1
            self.hashTable[i] = [start, start+w[i]-1]
        print self.hashTable
        """
        :type w: List[int]
        """
    
    def binarySearch(self, numberOnNumberLine, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        if(numberOnNumberLine >= self.hashTable[mid][0] and numberOnNumberLine <= self.hashTable[mid][1]):
            return mid
        if(numberOnNumberLine < self.hashTable[mid][0]):
            return self.binarySearch(numberOnNumberLine, low, mid-1)
        else:
            return self.binarySearch(numberOnNumberLine, mid+1, high)

    def pickIndex(self):
        numberOnNumberLine = random.randint(0, self.totalWeight-1)
        # now we just find what index it belongs to.
        return self.binarySearch(numberOnNumberLine, 0, len(self.hashTable)-1)
        """
        :rtype: int
        """

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
