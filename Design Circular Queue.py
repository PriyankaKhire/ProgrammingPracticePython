#  Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
class MyCircularQueue(object):

    def __init__(self, k):
        self.q = [None for i in range(k)]
        self.start = 0
        self.end = -1
        self.numElements = 0
        self.k = k
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        

    def enQueue(self, value):
        if(self.numElements == self.k):
            return False
        self.end = (self.end+1)%self.k
        self.q[self.end] = value
        self.numElements = self.numElements + 1
        return True
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        

    def deQueue(self):
        if(self.numElements == 0):
            return False
        self.q[self.start] = None
        self.start = (self.start+1)%self.k
        self.numElements = self.numElements - 1
        return True
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        

    def Front(self):
        if(self.numElements == 0):
            return -1
        return self.q[self.start]
        """
        Get the front item from the queue.
        :rtype: int
        """
        

    def Rear(self):
        if(self.numElements == 0):
            return -1
        return self.q[self.end]
        """
        Get the last item from the queue.
        :rtype: int
        """
        

    def isEmpty(self):
        if(self.numElements == 0):
            return True
        return False
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        

    def isFull(self):
        if(self.numElements == self.k):
            return True
        return False
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
