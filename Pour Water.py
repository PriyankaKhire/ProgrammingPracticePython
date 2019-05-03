#Pour Water
#https://leetcode.com/problems/pour-water/
import heapq
class Solution(object):
    #.               |             .               |
    #|              |             |              |               |
    #|              |             |              |               |
    #0---------i---------k---------j----------n
    #imagine the above senario: to solve this
    #we first need to heapify poles between i and k then poles between k and j
    #once we fill water between i and j and if there is more water remaining after that
    # we then need to repeat this senario for poles between 0 and i and j and n
    
    
    def findLeftSidePole(self, k, heights):
        if(k == 0 or k == len(heights)-1):
            return k, []
        leftIndexHeap = []
        #find left pole and add it to left heap
        left = k-1
        while(heights[k] > heights[left]):
            heapq.heappush(leftIndexHeap, (heights[left], left))
            left = left - 1
        return left, leftIndexHeap
    
    def findRightSidePole(self, k, heights):
        if(k == 0 or k == len(heights)-1):
            return k, []
        rightIndexHeap = []
        #find right pole
        right = k+1
        while(heights[k] > heights[right]):
            heapq.heappush(rightIndexHeap, (heights[right], right))
            right = right + 1
        return  right, rightIndexHeap

    def logic(self, leftK, rightK, K, heights, waterUnits):
        left, leftIndexHeap = self.findLeftSidePole(leftK, heights)
        right, rightIndexHeap = self.findRightSidePole(rightK, heights)
        print "Left pole is at index ", left, " right pole is at index ", right
        while(waterUnits > 0):
            waterUnits = waterUnits-1
            if((rightIndexHeap and leftIndexHeap and leftIndexHeap[0][0] <= rightIndexHeap[0][0]) or ((not rightIndexHeap) and leftIndexHeap)):
                print "Left heap top is ", leftIndexHeap[0]
                heights[leftIndexHeap[0][1]] = heights[leftIndexHeap[0][1]] + 1
                print "Popped out ", heapq.heappop(leftIndexHeap)
            elif((rightIndexHeap and leftIndexHeap and leftIndexHeap[0][0] > rightIndexHeap[0][0]) or ((not leftIndexHeap) and (rightIndexHeap))):
                print "Right heap top is ", rightIndexHeap[0]
                heights[rightIndexHeap[0][1]] = heights[rightIndexHeap[0][1]] + 1
                print "Popped out ", heapq.heappop(rightIndexHeap)
            else:
                heights[K] = heights[K]+1
                if(heights[K] > heights[left] and heights[K] > heights[right]):
                    print "breaking", heights
                    break
        return waterUnits, heights, left, right
                
    
    def pourWater(self, heights, V, K):
        left = K
        right = K
        while (V > 0):
            V, heights, left, right = self.logic(left, right,K, heights, V)
            print "hrer", V, heights, left, right
        print heights
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """

#Main
obj1 = Solution()
obj1.pourWater([2,1,1,2,1,2,2], 4, 3)
print "\n"
obj2 = Solution()
obj2.pourWater([1,2,3,4], 2, 2)
print "\n"
obj3 = Solution()
obj3.pourWater([3,1,3], 5, 1)
