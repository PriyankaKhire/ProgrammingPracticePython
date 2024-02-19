import heapq


class Solution(object):

    def heapApproach(self, nums, k):
        # key = element, value = frequency of element
        hashMap = {}
        # add to hash map
        for n in nums:
            if (n not in hashMap):
                hashMap[n] = 0
            hashMap[n] += 1
        # create a heap and add tuples to this heap
        heap = []
        for key in hashMap:
            tup = (hashMap[key], key)
            # add this tuple to heap of size k
            if (len(heap) < k):
                heapq.heappush(heap, tup)
            else:
                # if heap has reached k size
                top = heap[0]
                # if frequency of top element is less than frequency of current element
                if (top[0] < tup[0]):
                    # pop the top
                    heapq.heappop(heap)
                    # push the current element
                    heapq.heappush(heap, tup)
        return [x[1] for x in heap]

    def topKFrequent(self, nums, k):
        # return self.heapApproach(nums, k)
        return self.quickSort(nums, k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
