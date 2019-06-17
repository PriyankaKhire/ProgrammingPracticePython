# Pour Water
#https://leetcode.com/problems/pour-water/
class Solution(object):
    
    def findRightIndex(self, heights, index):
        i = index
        while(i<len(heights)-1 and heights[i+1] <= heights[i]):
            i = i+1
        #if the droplet is at the same level as its previous index, return there
        while(i > index and heights[i] == heights[i-1]):
            i = i-1
        return i
            
    def findLeftIndex(self, heights, index):
        i = index
        while(i>0 and heights[i-1] <= heights[i]):
            i = i-1
        #if the droplet is at same level as its previous index, return there
        while(i < index and heights[i] == heights[i+1]):
            i = i+1
        return i
            
    def pourWater(self, heights, volume, index):
        for drop in range(volume):            
            #find something on left
            left = self.findLeftIndex(heights, index)            
            if(heights[left] < heights[index]):                
                heights[left] = heights[left]+1
                continue
            #Find something on right
            right = self.findRightIndex(heights, index)            
            if(heights[right] < heights[index]):            
                heights[right] = heights[right]+1
                continue            
            heights[index] = heights[index]+1
        print heights
#Main
obj = Solution()
obj.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 2, 5)
print "*********************************************"
obj = Solution()
obj.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 2, 2)
print "*********************************************"
obj = Solution()
obj.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 10, 2)
print "*********************************************"
obj = Solution()
obj.pourWater([2,1,1,2,1,2,2], 4, 3)
