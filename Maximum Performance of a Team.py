# Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution(object):
    def __init__(self):
        self.performance = 0
    
    def recursion(self, speed, efficiency, selectedSpeed, selectedEfficiency, k, index):
        if (len(selectedSpeed) > k):
            return
        if (len(selectedSpeed) > 0):
            self.performance = max(self.performance, sum(selectedSpeed)*min(selectedEfficiency))
        for i in range(index, len(speed)):
            self.recursion(speed, efficiency, selectedSpeed+[speed[i]], selectedEfficiency+[efficiency[i]], k, i+1)
            
    def maxPerformance(self, n, speed, efficiency, k):
        self.recursion(speed, efficiency, [], [], k, 0)
        return self.performance
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        
