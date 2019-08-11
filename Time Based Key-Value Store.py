#Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap(object):

    def __init__(self):
        self.hash = {}
        """
        Initialize your data structure here.
        """
        

    def set(self, key, value, timestamp):
        if not(key in self.hash):
            self.hash[key] = [[timestamp, value]]
        else:
            self.hash[key].append([timestamp, value])
            
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
    
    def binarySearch(self, key, array, low, high):
        #print array, 'key', key, 'low', low, 'high', high
        if(low >= high):
            if(array[low][0] <= key):
                return array[low][1]
            if(low-1 >= 0):
                return array[low-1][1]
            return ""
        mid = (low+high)/2
        #print 'mid', mid
        if(array[mid][0] == key):
            return array[mid][1]
        if(array[mid][0] < key):
            return self.binarySearch(key, array, mid+1, high)
        else:
            return self.binarySearch(key, array, low, mid-1)
        
        

    def get(self, key, timestamp):
        if not key in self.hash:
            return None
        return self.binarySearch(timestamp, self.hash[key], 0, len(self.hash[key])-1)
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
