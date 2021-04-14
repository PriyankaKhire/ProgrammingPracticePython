# Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = []
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        self.queue.append(val)
        if (len(self.queue) > self.size):
            self.queue.pop(0)
        return sum(self.queue)/float(len(self.queue))
        """
        :type val: int
        :rtype: float
        """
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
