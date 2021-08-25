# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def addToHeap(self, numHash):
        heap = []
        # add to heap in form of tuple, (frequency, number)
        # in python 2 there is no max heap, in order to get correct answer, I negated the frequency so top frequency element is on top of min heap.
        for key in numHash:
            heapq.heappush(heap, (-numHash[key], key)) 
        return heap
        
    def addToHash(self, nums):
        numHash = {}
        # add all numbers to has, with key: number, value: frequency
        for n in nums:
            if n not in numHash:
                numHash[n] = 0
            numHash[n] = numHash[n] + 1
        return numHash
            
    def topKFrequent(self, nums, k):
        hashMap = self.addToHash(nums)
        heap = self.addToHeap(hashMap)
        topK = []
        for i in range(k):
            (frequency, element) = heapq.heappop(heap)
            topK.append(element)
        return topK
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
