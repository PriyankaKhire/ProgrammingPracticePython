# Course Schedule
# https://leetcode.com/problems/course-schedule/
class Solution(object):
    def __init__(self):
        self.graphMatrix = []
    
    def findCycle(self, courseNumber, stack, visited):
        for course in range(len(self.graphMatrix)):
            if(self.graphMatrix[courseNumber][course] == 1 and not(course in visited)):
                if(course in stack):
                    return True
                stack.append(course)
                if(self.findCycle(course, stack, visited)):
                    return True
                stack.pop()
        visited.append(courseNumber)
                
    
    def fillMatrix(self, prerequisites):
        for edgeList in prerequisites:
            self.graphMatrix[edgeList[1]][edgeList[0]] = 1

    def isCycle(self, numCourses):
        for course in range(numCourses):
            if(self.findCycle(course, [course], [])):
                return True
        return False
    
    def canFinish(self, numCourses, prerequisites):
        self.graphMatrix = [[0 for col in range(numCourses)] for row in range(numCourses)]
        self.fillMatrix(prerequisites)
        return not(self.isCycle(numCourses))
        
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
# Main
obj = Solution()
print obj.canFinish(7, [[1,0],[2,0],[3,0],[4,2],[5,3],[5,4],[6,5]])

#print obj.canFinish(2, [[1,0],[0,1]])
