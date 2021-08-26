# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):

    def __init__(self):
        # holds all elements greater than median
        self.minHeap = []
        # holds all elements smaller than median.
        self.maxHeap = []
        """
        initialize your data structure here.
        """
    
    def addToMinHeap(self, num):
        # add number to min heap
        heapq.heappush(self.minHeap, num)
        # if length of heap is more then pop the element and add to max heap
        if (len(self.minHeap) > len(self.maxHeap)+1):
            element = heapq.heappop(self.minHeap)
            self.addToMaxHeap(element)
    
    def addToMaxHeap(self, num):
        # add number to max heap
        self.maxHeap.append(num)
        heapq._heapify_max(self.maxHeap)
        # if length of heap is more then pop the item and add to min Heap
        if (len(self.maxHeap) > len(self.minHeap)+1):
            element = self.maxHeap.pop(0)
            heapq._heapify_max(self.maxHeap)
            self.addToMinHeap(element)
        
    def addNum(self, num):
        # if both heaps are empty
        if ((not self.minHeap) and (not self.maxHeap)):
            self.addToMinHeap(num)
            return
        # if max heap is empty but min heap is not.
        if ((not self.maxHeap) and self.minHeap):
            # if top of min heap < num (because min heap needs to hold elements greater than median)
            if (self.minHeap[0] < num):
                # pop the top from min heap and add to max heap
                topMinElement = heapq.heappop(self.minHeap)
                self.addToMaxHeap(topMinElement)
            # add current element to min heap
            self.addToMinHeap(num)
            return
        # if both heaps have elements
        if (self.minHeap and self.maxHeap):
            # max heap contains elements from 0 to median
            if (num < self.maxHeap[0]):
                self.addToMaxHeap(num)
            else:
                self.addToMinHeap(num)
        """
        :type num: int
        :rtype: None
        """
        
    def findMedian(self):
        if (len(self.minHeap) == len(self.maxHeap)):
            return float(self.minHeap[0]+self.maxHeap[0])/float(2)
        if (len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]
        return self.maxHeap[0]
        """
        :rtype: float
        """
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
