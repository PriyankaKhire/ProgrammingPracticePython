# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        # Sort all intervals by start time
        intervals = sorted(intervals)
        # Create a min heap
        heap = []
        # start add elements to heap
        for i in intervals:
            if not heap:
                # add only interval ending
                heap.append(i[1])
                continue
            # check the top element of heap
            top = heap[0]
            # if top element is > start of this interval then add ending of this interval
            if (top > i[0]):
                heapq.heappush(heap, i[1])
            else:
                # pop the top and add this new interval ending
                heapq.heappop(heap)
                heapq.heappush(heap, i[1])
            # print "Heap", heap
        return len(heap)
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
