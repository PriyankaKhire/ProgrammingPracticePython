# Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap(object):

    def __init__(self):
        # key = key, value = [(timeStamp, value)]
        self.hashMap = {}

    def set(self, key, value, timestamp):
        if (key not in self.hashMap):
            self.hashMap[key] = []
        # create tuple
        tup = (timestamp, value)
        # add to hash map
        self.hashMap[key].append(tup)
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
    
    def binarySearch(self, target, array):
        start = 0
        end = len(array) - 1
        while(start < end):
            mid = (start+end)/2
            (ts, val) = array[mid]
            if (target == ts):
                return val
            if (target < ts):
                # go left
                end = mid-1
                continue
            if (ts < target):
                # get the mid+1 tuple
                (ts1, val1) = array[mid+1]
                if (target < ts1):
                    return val
                # go right
                start = mid+1
        if (start == end):
            (ts, val) = array[start]
            if (ts <= target):
                return val

    def get(self, key, timestamp):
        # if key not found in hash map
        if (key not in self.hashMap):
            return ""
        val = self.binarySearch(timestamp, self.hashMap[key])
        if (val == None):
            return ""
        return val
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
