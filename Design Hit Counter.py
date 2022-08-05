# Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/
class HitCounter(object):

    def __init__(self):
        # hit counter for 300 seconds = 5 mins
        self.queue = [0 for i in range(300)]
        self.hitCount = 0
        # keeping track of start of 5 min window
        self.startTimeStamp = 0
        self.endTimeStamp = 300
        
    # reduce queue by number of spaces
    def reduceQueueSize(self, spaces):
        for i in range(spaces):
            # reduce hit count by number in queue
            self.hitCount -= self.queue.pop(0)
            
    # increase queue size by number of spaces
    def increaseQueueSize(self, spaces):
        for i in range(spaces):
            self.queue.append(0)
    
    def adjustQueue(self, timestamp):
        if (timestamp > self.endTimeStamp):
            # if timestamp difference is greater than 5 mins or 300 seconds then make queue empty and reset hit counter to 0
            if (timestamp - self.endTimeStamp > 300):
                self.queue = [0 for i in range(300)]
                self.hitCount = 0
            else:
                # reduce tail of queue by timestamp - endTimeStamp
                self.reduceQueueSize(timestamp - self.endTimeStamp)
                # increase head of queue size by timestamp - endTimeStamp
                self.increaseQueueSize(timestamp - self.endTimeStamp)
            # increase start time
            self.startTimeStamp += timestamp - self.endTimeStamp
            # increase end time
            self.endTimeStamp = timestamp

    def hit(self, timestamp):
        self.adjustQueue(timestamp)
        # add hit at time stamp
        # calculate index of timestamp in hit counter queue
        index = timestamp - (self.endTimeStamp - 300) -1
        self.queue[index] += 1
        # increment hit
        self.hitCount += 1
        """
        :type timestamp: int
        :rtype: None
        """
        
    def getHits(self, timestamp):
        self.adjustQueue(timestamp)
        return self.hitCount
        """
        :type timestamp: int
        :rtype: int
        """

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
