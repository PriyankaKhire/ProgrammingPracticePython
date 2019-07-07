#Container With Most Water
#https://leetcode.com/problems/container-with-most-water/
class BruteForce(object):
    def maxArea(self, height):
        maxArea = 0
        for start in range(len(height)-1):
            for end in range(start+1, len(height)):
                currentArea = min(height[start], height[end])*(end-start)
                maxArea = max(maxArea, currentArea)
        print maxArea

#It's not realistic to come up with this approch in a 45 min interview.
class LeetcodeApproch(object):
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        maxArea = 0
        while(start < end):
            currentArea = min(height[start], height[end])*(end-start)
            maxArea = max(maxArea, currentArea)
            if(height[start] < height[end]):
                start = start + 1
            else:
                end = end - 1
        print maxArea
        
#Main
obj = BruteForce()
obj.maxArea([1,8,6,2,5,4,8,3,7])

obj = LeetcodeApproch()
obj.maxArea([1,8,6,2,5,4,8,3,7])
