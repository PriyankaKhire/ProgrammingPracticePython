# Course Schedule
# https://leetcode.com/problems/course-schedule/

class Solution(object):
    def __init__(self):
        self.noIncomingEdges = []
        # key: edge; value: nodes from where we have incoming edges.
        self.adjacencyListIncoming = {}
        # key: edge; value: nodes from where we have outgoing edges.
        self.adjacencyListOutgoing = {}
    
    def createAdjacencyList(self, numCourses, prerequisites):
        # fill out the adjacency list according to number of cousese.
        self.adjacencyListIncoming = {course: [] for course in range(numCourses)}
        self.adjacencyListOutgoing = {course: [] for course in range(numCourses)}
        # get all the outgoing edges.
        for courses in prerequisites:
            self.adjacencyListOutgoing[courses[1]].append(courses[0])
        # get all the incoming edges.
        for courses in prerequisites:
            self.adjacencyListIncoming[courses[0]].append(courses[1])
    
    def topologicalSort(self):
        sortOrder = []
        # get all the edges with no incoming edges
        for course in self.adjacencyListIncoming:
            if (not self.adjacencyListIncoming[course]):
                self.noIncomingEdges.append(course)
        # while the incoming edges list is not empty
        while(self.noIncomingEdges):
            # get the top edge
            top = self.noIncomingEdges.pop(0)
            # add top to sorted list
            sortOrder.append(top)
            # get all the outgoing edges from it and remove their incoming edges
            for edge in self.adjacencyListOutgoing[top]:
                self.adjacencyListIncoming[edge].remove(top)
                # if the current edge does not have anymore incoming edges then add it to noIncomingEdges list
                if (not self.adjacencyListIncoming[edge]):
                    self.noIncomingEdges.append(edge)
        # sort order indicates the edges you have visited.
        return sortOrder
    
    def checkVisitedNodes(self, visitedNodes, numCourses):
        # if we have visited all nodes that means all prerequisites are satisfied.
        # in case of a cycle the sort order from topological sort would be empty.
        for course in range(numCourses):
            if (course not in visitedNodes):
                return False
        return True
        
    def canFinish(self, numCourses, prerequisites):
        self.createAdjacencyList(numCourses, prerequisites)
        visitedNodes = self.topologicalSort()
        return self.checkVisitedNodes(visitedNodes, numCourses)
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
