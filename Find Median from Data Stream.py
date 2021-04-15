# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
import heapq

class MedianFinder:

    def __init__(self):
        # Keeps track of higher values
        self.minHeap = []
        # Keeps track of lower values
        self.maxHeap = []
        """
        initialize your data structure here.
        """
    
    def addToMaxHeap(self, element):
        print ("Adding element to max heap", element)
        self.maxHeap.append(element)
        heapq._heapify_max(self.maxHeap)
    
    def addToMinHeap(self, element):
        print ("Adding element to min heap", element)
        self.minHeap.append(element)
        heapq.heapify(self.minHeap)
    
    def balenceHeaps(self):
        print ("Balencing heaps", self.maxHeap, self.minHeap)
        # Min heap is supposed to contain larger elements 
        # Max heap is supposed to contain smaller elements
        if (self.maxHeap[0] > self.minHeap[0]):
            element = heapq._heappop_max(self.maxHeap)
            self.addToMinHeap(element)
        if(len(self.maxHeap) > len(self.minHeap)+1):
            element = heapq._heappop_max(self.maxHeap)
            self.addToMinHeap(element)
            return
        if(len(self.minHeap) > len(self.maxHeap)+1):
            element = heapq.heappop(self.minHeap)
            self.addToMaxHeap(element)
            return

    def addNum(self, num: int) -> None:
        print ("Adding", num)
        if not self.maxHeap:
            self.addToMaxHeap(num)
            return
        if not self.minHeap:
            self.addToMinHeap(num)
            # we need to balence here so that from beginning it self the roots are proper.
            self.balenceHeaps()
            return
        if (num > self.maxHeap[0]):
            self.addToMinHeap(num)
        else: 
            self.addToMaxHeap(num)
        self.balenceHeaps()
        print ("maxHeap",self.maxHeap, "minHeap", self.minHeap)

    def findMedian(self) -> float:
        print ("finding median")
        if (self.maxHeap and not self.minHeap):
            return self.maxHeap[0]
        if (self.minHeap and not self.maxHeap):
            return self.minHeap[0]
        if (len(self.maxHeap) == len(self.minHeap)):
            return (self.maxHeap[0]+self.minHeap[0])/2
        if (len(self.maxHeap) > len(self.minHeap)):
            return self.maxHeap[0]
        return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
