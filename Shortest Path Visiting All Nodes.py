#Shortest Path Visiting All Nodes
#https://leetcode.com/problems/shortest-path-visiting-all-nodes/
class DFS(object):

    def recurrse(self, graph, node, visited, output):
        print output
        for neighbor in graph[node]:
            if(visited[neighbor] == False and not(neighbor in output)):
                output.append(neighbor)
                self.recurrse(graph, neighbor, visited, output)
                output.append(node)
        visited[node] = True
        return

        
    def shortestPathLength(self, graph):
        visited = [False for i in range(len(graph))]
        self.recurrse(graph, 1, visited, [1])
        """
        :type graph: List[List[int]]
        :rtype: int
        """
#Main
obj1 = DFS()
obj1.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])

#obj2 = DFS()
#obj2.shortestPathLength([[1,2,3],[0],[0],[0]])
