# Minimum number of intervals to cover the target interval
# https://www.geeksforgeeks.org/minimum-number-of-intervals-to-cover-the-target-interval/
class Solution(object):
    def minIntervals(self, intervals, targetInterval):
        # Sort the intervals
        intervals = sorted(intervals)
        # Assign first interval to start and end
        start = intervals[0][0]
        end = intervals[0][1]
        count = 1
        # The first interval itself doesn't cover our target interval
        if (start > targetInterval[0]):
            return -1
        for i in range(1, len(intervals)):
            if (end >= targetInterval[1]):
                break
            if (start == intervals[i][0]):
                end = max(end, intervals[i][1])
                continue
            if (end >= intervals[i][1]):
                continue
            count += 1
            start = intervals[i][0]
            end = intervals[i][1]
        return count
            
        

# Main
obj = Solution()
print obj.minIntervals([[1, 3], [2, 4], [2, 10], [2, 3], [1, 1]], [1, 10])
print obj.minIntervals([[2,6], [7,9],[3,5],[6,10]], [1,4])
