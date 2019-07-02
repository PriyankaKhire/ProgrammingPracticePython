#Meeting Rooms II
#https://leetcode.com/problems/meeting-rooms-ii/
import heapq
class Solution(object):
    def logic(self, intervals):
        minHeap = []
        for interval in intervals:
            if not minHeap:
                heapq.heappush(minHeap, interval[1])
                continue
            #if end time of top of heap is greater than start time of current interval, then push current interval into heap
            if(minHeap[0] > interval[0]):
                heapq.heappush(minHeap, interval[1])
            else:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, interval[1])
        #at the end what ever is inside the heap are the number of meeting rooms that we reqire.
        return len(minHeap)
    
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        return self.logic(intervals)
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
#Main
obj = Solution()
print obj.minMeetingRooms([[4, 7], [3, 4], [0, 2], [1,3], [2, 8], [5, 8]])
