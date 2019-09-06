# Median in a stream of integers (running integers)
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
import heapq

class Solution(object):
    def __init__(self):
        # to keep numbers that are greater than median
        self.minHeap = []
        # to keep numbers that are smaller than median
        self.maxHeap = []

    def addNumberToMaxHeap(self, number):
        if(len(self.maxHeap) <= len(self.minHeap)):
            self.maxHeap.append(number)
            heapq._heapify_max(self.maxHeap)
        else:
            # first push our element to max heap
            self.maxHeap.append(number)
            heapq._heapify_max(self.maxHeap)
            # max heap has way too many elements, so we need to pop element from max heap and add it to min heap to balance it out
            otherNum = self.maxHeap.pop(0)
            heapq._heapify_max(self.maxHeap)
            # the number we popped from max heap 
            heapq.heappush(self.minHeap, otherNum)

    def addNumberToMinHeap(self, number):
        if(len(self.minHeap) <= len(self.maxHeap)):
            heapq.heappush(self.minHeap, number)
        else:
            # first push element onto min heap
            heapq.heappush(self.minHeap, number)
            # min heap has more elements than max heap, we need to pop element from min heap and add it to max heap
            otherNum = heapq.heappop(self.minHeap)
            # since the number was popped from min heap we need to add it to max heap,
            self.maxHeap.append(otherNum)
            heapq._heapify_max(self.maxHeap)
            

    def addNumber(self, number):
        print self.maxHeap, self.minHeap
        # if its the first number
        if(not self.minHeap and not self.maxHeap):
            self.minHeap.append(number)
            return
        # if its the second number
        if(not self.maxHeap):
            if(number < self.minHeap[0]):
                self.maxHeap.append(number)
            else:
                # add the number in minHeap to max heap
                otherNum = self.minHeap.pop()
                self.maxHeap.append(otherNum)
                # add current number to minHeap
                self.minHeap.append(number)
            return
        # from third number onwards
        # 1) which heap the number belongs to ?
        if(number < self.maxHeap[0]):
            # number belongs to max heap
            self.addNumberToMaxHeap(number)
        else:
            # number belongs to minHeap
            self.addNumberToMinHeap(number)

    def findMedian(self):
        if(not self.maxHeap and not self.minHeap):
            return
        if(not self.maxHeap and self.minHeap):
            return self.minHeap[0]
        if(not self.minHeap and self.maxHeap):
            return self.maxHeap[0]
        # If both heaps have same number of elements then the median is average of their roots
        if(len(self.minHeap) == len(self.maxHeap)):
            return (self.minHeap[0]+self.maxHeap[0])/float(2)
        if(len(self.minHeap) > len(self.maxHeap)):
            return self.minHeap[0]
        return self.maxHeap[0]

# Main
obj = Solution()
print obj.findMedian()
obj.addNumber(15)
print obj.findMedian()
obj.addNumber(5)
print obj.findMedian()
obj.addNumber(1)
print obj.findMedian()
obj.addNumber(3)
print obj.maxHeap, obj.minHeap
print obj.findMedian()
