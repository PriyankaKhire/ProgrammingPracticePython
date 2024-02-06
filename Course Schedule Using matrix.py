# Course Schedule
# https://leetcode.com/problems/course-schedule/description/

class Solution(object):
    def __init__(self):
        self.graph = []
    
    def createGraph(self, numCourses, preReq):
        self.graph = [[0 for col in range(numCourses)] for row in range(numCourses)]
        for c in preReq:
            # there is an edge from c[1] to c[0]
            self.graph[c[1]][c[0]] = 1
        
    def display(self):
        for row in range(len(self.graph)):
            for col in range(len(self.graph[0])):
                print self.graph[row][col],
            print ""
        print ""

    def topologicalSort(self, node, visited, stack):
        if (node in visited):
            return False
        # mark the node visited
        visited.append(node)
        # get all children of node
        for child in range(len(self.graph)):
            # we wanna make sure child is not in stack, it means it's already been explored
            # but if the child is not in stack but in visited that means there's a cycle
            if (self.graph[node][child] == 1 and (child not in stack)):
                if not(self.topologicalSort(child, visited, stack)):
                    return False
        # when all children of the current node are explored
        stack.append(node)
        return True

    
    def canFinish(self, numCourses, prerequisites):
        # create graph
        self.createGraph(numCourses, prerequisites)
        #self.display()
        visited = []
        outputStack = []
        for course in range(numCourses):
            if (course in outputStack):
                continue
            if not (self.topologicalSort(course, visited, outputStack)):
                return False
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
