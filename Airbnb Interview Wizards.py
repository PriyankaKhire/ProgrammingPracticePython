# -*- coding: cp1252 -*-
#Wizards
'''
There are 10 wizards at a wizard meetup.
Each wizard has levels between 0 – 9 (the index of the input)
and  knows a few other wizards there.
Your job is to find the cheapest way for wizard 0 to meet wizard 9.
Introductions have a cost that equals the square of the difference in levels.

Goal: Level 0 wizard wants to meet level 9 using the fewest possible magic points.

Cost: square of difference of levels

The index of the array represents the level (0-9). 
the value is an array with the index of the other people each person knows.

Note that relationships are one directional (e.g. 2 can introduce you to 3 but not vice versa). 

Example:
Input:
Wizards = [
    [1, 2, 3],  # wizard0 knows wizards 1, 2, 3
    [8, 6, 4], # wizard1 knows wizards 8, 6, 4
    [7, 8, 3], # wizard2 knows wizards 7, 8, 3
    [8, 1],     # and so on...
    [6],
    [8, 7],
    [9, 4],
    [4, 6],
    [1],
    [1, 4]
]

Output:
Min cost: 23 = (0-1)^2 + (1-4)^2 + (4-6)^2 + (6-9)^2
Min path: [0, 1, 4, 6, 9]. 
'''
class Solution(object):
    def __init__(self):
        self.matrix = []
        
    def constructGraphMatrix(self, wizards):
        self.matrix = [[None for col in range(len(wizards))] for row in range(len(wizards))]
        for wizard in range(len(wizards)):
            for friend in wizards[wizard]:
                self.matrix[wizard][friend] = (wizard-friend)**2

    def getUnvisitedLeastCostVertex(self, cost, visited):
        vertex = None
        for v in range(len(cost)):
            if(v in visited):
                continue
            if(vertex == None or cost[v] < cost[vertex]):
                vertex = v
        return vertex

    def dijkastra(self, visited, visitedFromVertex, cost, destination):
        if(destination in visited):
            return
        # get the vertex with least cost that is not visited
        currVertex = self.getUnvisitedLeastCostVertex(cost, visited)
        # get all its neighbours
        for friend in range(len(self.matrix)):
            if(not(friend in visited) and self.matrix[currVertex][friend] != None):
                if(cost[currVertex]+self.matrix[currVertex][friend] < cost[friend]):
                    cost[friend] = cost[currVertex]+self.matrix[currVertex][friend]
                    visitedFromVertex[friend] = currVertex
        # mark current vertex visited
        visited.append(currVertex)
        self.dijkastra(visited, visitedFromVertex, cost, destination)
        
    def getCost(self, wizards):
        self.constructGraphMatrix(wizards)
        cost = [float("inf") for i in range(len(wizards))]
        cost[0] = 0
        visitedFromVertex = [None for i in range(len(wizards))]
        self.dijkastra([], visitedFromVertex, cost, 9)
        print "Min Cost",cost[9]
        path = []
        currVertex = 9
        while(currVertex != None):
            path.append(currVertex)
            currVertex = visitedFromVertex[currVertex]
        path.reverse()
        print "Min Path", path

# Main
wizards = [
    [1, 2, 3],  
    [8, 6, 4], 
    [7, 8, 3], 
    [8, 1],     
    [6],
    [8, 7],
    [9, 4],
    [4, 6],
    [1],
    [1, 4]
    ]
obj = Solution()
obj.getCost(wizards)
