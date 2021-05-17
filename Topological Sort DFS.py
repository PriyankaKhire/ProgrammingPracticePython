# Topological Sort DFS
# https://leetcode.com/discuss/general-discussion/1078072/introduction-to-topological-sort
class TopologicalSort(object):
    def isIndegreeZero(self, graph, node):
        for n in range(len(graph)):
            if (graph[n][node] == 1):
                return False
        return True
    
    def findNodesWithZeroIndegree(self, graph):
        nodes = []
        for currentNode in range(len(graph)):
            if (self.isIndegreeZero(graph, currentNode)):
                nodes.append(currentNode)
        return nodes
    
    def createGraph(self, numberOfNodes, nodes):
        graph = [[0 for col in range(numberOfNodes)] for row in range(numberOfNodes)]
        for n in nodes:
            graph[n[0]][n[1]] = 1
        return graph
    
    def dfs(self, currNode, graph, visited, answer):
        # visit the current node
        visited[currNode] = True
        # get all unvisited neighbours.
        for n in range(len(graph)):
            if (graph[currNode][n] == 1 and visited[n] == False):
                self.dfs(n, graph, visited, answer)
        answer.append(currNode)
    
    def graphColoring(self, matrix, unExploredNodes, partiallyExploredNodes, completelyExploredNodes, currentNode):
        #print "Current Node", currentNode, "Un explored", unExploredNodes, "Partially explored", partiallyExploredNodes, "Completely explored", completelyExploredNodes
        # Remove from unExplored nodes and put it in partially explored nodes.
        unExploredNodes.remove(currentNode)
        # Put the current node in partially explored set of nodes
        partiallyExploredNodes.append(currentNode)
        # Get all the neighbors of the current node and visit them
        for n in range(len(matrix)):
            if(matrix[currentNode][n] == 1):
                # But if the neighbor is in partially explored nodes then there is a cycle
                if(n in partiallyExploredNodes):
                    return True
                # Else if n is not completely explored visit it.
                if not(n in completelyExploredNodes):
                    if(self.graphColoring(matrix, unExploredNodes, partiallyExploredNodes, completelyExploredNodes, n)):
                        return True
        # Remove from partially explored nodes
        partiallyExploredNodes.remove(currentNode)
        completelyExploredNodes.append(currentNode)
    
    def detectCycle(self, matrix):
        unExploredNodes = [i for i in range(len(matrix))] # Unexplored nodes
        partiallyExploredNodes = [] # Partially explored nodes
        completelyExploredNodes = [] # Completely explored nodes
        while(unExploredNodes):
            startNode = unExploredNodes[0]
            if(self.graphColoring(matrix, unExploredNodes, partiallyExploredNodes, completelyExploredNodes, startNode)):
                return True
        
        
    
    def sort(self, numCourses, prerequisites):
        graph = self.createGraph(numCourses, prerequisites)
        #print graph
        # detect cycle
        if (self.detectCycle(graph)):
            return []
        startNodes = self.findNodesWithZeroIndegree(graph)
        visited = [False for i in range(numCourses)]
        answer = []
        for node in startNodes:
            self.dfs(node, graph, visited, answer)
        print answer
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        

# Main
numberOfNodes = 7
nodes = [[1, 2], [1, 4], [2, 3], [4, 5], [4, 6], [5, 6]]
'''
 0           ---> 5
            /       |
          /        \/
 1---->4------->6
 |       |
\/      |                
 2<----|
  |
 \/
  3  
'''
obj = TopologicalSort()
obj.sort(numberOfNodes, nodes)
print "*"*50
numberOfNodes = 6
nodes = [[2,3],[3,1],[4,1],[4,0],[5,0],[5,2]]
'''
  5       4
 /  \   /  \
2     0      1
 \           /
   \      /
       3
'''
obj = TopologicalSort()
obj.sort(numberOfNodes, nodes)

print "*"*50
numberOfNodes = 100
nodes = [[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]
obj = TopologicalSort()
obj.sort(numberOfNodes, nodes)

