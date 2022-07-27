# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def __init__(self):
        # key = element val = count
        self.hashMap = {}
    
    def addToHashMap(self, nums):
        for n in nums:
            if (n not in self.hashMap):
                self.hashMap[n] = 0
            self.hashMap[n] += 1
    
    def addToHeap(self, k):
        minHeap = []
        for key in self.hashMap:
            if (len(minHeap) == k):
                # if top of heap count is less than current count then remove top element and add current element
                if (minHeap[0][0] < self.hashMap[key]):
                    # remove top element
                    heappop(minHeap)
                    # add current element
                    heappush(minHeap, (self.hashMap[key], key))
            else:
                heappush(minHeap, (self.hashMap[key], key))
        return minHeap
    
    def extractElements(self, heap):
        elements = []
        for tup in heap:
            elements.append(tup[1])
        return elements
        
    def topKFrequent(self, nums, k):
        self.addToHashMap(nums)
        heap = self.addToHeap(k)
        return self.extractElements(heap)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
