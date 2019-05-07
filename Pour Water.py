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
class Solution2(object):
    #inspired by http://zxi.mytechroad.com/blog/simulation/leetcode-755-pour-water/
    def findLeftHole(self, heights, index):
        print "Finding left hole"
        hole = index-1
        while(hole >= 0):
            print "Currently at hole index ", hole," with height ", heights[hole]
            if(heights[hole] <= heights[index] and heights[hole-1] <= heights[hole]):
                print "Finding next hole"
                hole = hole - 1
            elif(heights[hole] <= heights[index] and heights[hole-1] > heights[hole]):
                print "breaking"
                break
            else:
                break
        if(heights[hole] < heights[index]):
            print "Returning hole ", hole
            return hole
        return -1

    def findRightHole(self, heights, index):
        print "Finding right hole"
        hole = index+1
        while(hole < len(heights)-1):
            print "Currently at hole index ", hole," with height ", heights[hole]
            if(heights[hole] <= heights[index] and heights[hole+1] <= heights[hole]):
                print "Finding next hole"
                hole = hole + 1
            elif(heights[hole] <= heights[index] and heights[hole+1] > heights[hole]):
                print "breaking"
                break
            else:
                break
        if(heights[hole] < heights[index]):
            print "Returning hole ", hole
            return hole
        return -1
    
    def pourWater(self, heights, V, K):
        for waterDrop in range(V):
            print heights
            print "Pouring water droplet number ", waterDrop
            #find left hole
            leftHole = self.findLeftHole(heights, K)
            rightHole = self.findRightHole(heights, K)
            print "Left hole is ", leftHole, " right Hole is ", rightHole
            if(leftHole != -1 and rightHole != -1):
                print "we have found 2 holes less than current index hole"
                if(heights[leftHole] <= heights[rightHole]):
                    heights[leftHole] = heights[leftHole] + 1
                else:
                    heights[rightHole] = heights[rightHole] + 1
            elif((leftHole == -1) and rightHole != -1):
                print "Left hole ain't there but right is"
                heights[rightHole] = heights[rightHole] + 1
            elif((rightHole == -1) and leftHole != -1):
                print "Right hole ain't there but left is "
                heights[leftHole] = heights[leftHole] + 1
            else:
                print "Filling current index"
                heights[K] = heights[K] + 1
        print heights
        

#Main
#obj1 = Solution()
#obj1.pourWater([2,1,1,2,1,2,2], 4, 3)
obj12 = Solution2()
obj12.pourWater([2,1,1,2,1,2,2], 4, 3)
print "\n"
#obj2 = Solution()
#obj2.pourWater([1,2,3,4], 2, 2)
obj22 = Solution2()
obj22.pourWater([1,2,3,4], 2, 2)
print "\n"
#obj3 = Solution()
#obj3.pourWater([3,1,3], 5, 1)
obj32 = Solution2()
obj32.pourWater([3,1,3], 5, 1)
