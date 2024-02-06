# Finding Cycles in a graph
'''
This algorithem also considers following as cycles
1 --> 2 <--/ 
\            /
 \         /
   \--> 3

      4
     / \
   /    \
  \/    \/
  1      2
  \      /
   \   /
    \|/
    3
'''

class Solution(object):
    def __init__(self):
        self.matrix = []
    
    def createMatrix(self, prereq, numCourses):
        self.matrix = [[0 for col in range(numCourses)] for row in range(numCourses)]
        for course in prereq:
            self.matrix[course[1]][course[0]] = 1
    
    def displayMatrix(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                print self.matrix[row][col],
            print ""
        print ""
    
    def areThereCycle(self, node, visited):
        print "visiting node", node, visited
        if (node in visited):
            return True
        for children in range(len(self.matrix[0])):
            print children, len(self.matrix[0])
            # for back edges
            if (self.matrix[node][children] == 1 and children == node):
                return True
            if (self.matrix[node][children] == 1):
                # Mark it visited
                visited.append(node)
                if (self.areThereCycle(children, visited)):
                    return True
        # if a leaf node
        visited.append(node)

    def canFinish(self, numCourses, prerequisites):
        self.createMatrix(prerequisites, numCourses)
        self.displayMatrix()
        # check for cycles
        for course in range(numCourses):
            # Need to clear out visited array every time otherwise it will give wrong answer about cycles
            # this is done for cases like 0 <-- 1
            visited = []
            if (course not in visited):
                print "On course", course
                if (self.areThereCycle(course, visited)):
                    return False
            print "visited", visited
        return True
        """    
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
