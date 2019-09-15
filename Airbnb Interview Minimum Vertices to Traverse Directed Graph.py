#  Cover all vertices with the least number of vertices
# https://leetcode.com/discuss/interview-question/124861/digraph-cover-all-vertices-with-the-least-number-of-vertices
class Solution(object):
    def bfs(self, graphMatrix, vertex):
        queue = [vertex]
        # Maintaining a hash set of visited vertices
        visited = [vertex]
        while(queue):
            top = queue.pop(0)
            # find all unvisited vertices neighbor of current vertex
            for v in range(len(graphMatrix)):
                if(graphMatrix[top][v] == 1 and not(v in visited)):
                    visited.append(v)
                    queue.append(v)
        return visited

    def backtrack(self, index, verticesCovered, hashTable, currSetOfVertices, allSetsOfVertices):
        if(len(verticesCovered) == len(hashTable)):
            allSetsOfVertices.append(currSetOfVertices)
            return
        for i in range(index, len(hashTable)):
            # the list(set(list))) avoids duplicate vertices form entering the list of covered vertices
            self.backtrack(i+1, list(set(verticesCovered+hashTable[i])), hashTable, currSetOfVertices+[i], allSetsOfVertices)

    def maxVertices(self, graphMatrix):
        hashTable = {}
        # get list of all vertices that can be visited from current vertex
        for vertex in range(len(graphMatrix)):
            hashTable[vertex] = self.bfs(graphMatrix, vertex)
        # get set of vertices that visit all other vertices.
        allSetsOfVertices = []
        self.backtrack(0, [], hashTable, [], allSetsOfVertices)
        # get the set with least number of vertices
        minSet = allSetsOfVertices[0]
        for verticeSet in allSetsOfVertices:
            if(len(verticeSet) < len(minSet)):
                minSet = verticeSet
        print len(minSet)

# Main
# in this solution row goes to col and not other way round.
g = [[1, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
obj = Solution()
obj.maxVertices(g) # result 2

g = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0]
    ]
obj = Solution()
obj.maxVertices(g) #result 1

g = [
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0]
    ]
obj = Solution()
obj.maxVertices(g) #result 1

g = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0 ,0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0 ,0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0 ,0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]
obj = Solution()
obj.maxVertices(g) #result 3

g = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]
obj = Solution()
obj.maxVertices(g) #result 1

g = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
    ]
obj = Solution()
obj.maxVertices(g) #result 2
