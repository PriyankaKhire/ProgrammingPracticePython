# Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# took hints from https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/178744/Python-BFS-solution-with-optimization.-Beats-100
# and https://www.youtube.com/watch?time_continue=21&v=Vo3OEN2xgwk
# this is very similar to the sliding window approch that you have coded.
class QNode(object):
    def __init__(self, vertex, state):
        self.vertex = vertex
        self.state = state
        self.previousPath = [vertex]
        
class Solution(object):
    # returns true if Vertex1 -> Vertex2
    def edgeBetweenVertex1andVertex2(self, graph, vertex1, vertex2):
        if(vertex2 in graph[vertex1]):
            return True
        return False

    def createQNode(self, vertex, state):
        return QNode(vertex, state)

    def turnOnNthBitOfState(self, state, n):
        return state[:n]+'1'+state[n+1:]

    def bfs(self, graph, originVertex):
        qnode = self.createQNode(originVertex, '0'*len(graph))
        queue = [qnode]
        print "Our origin node looks like this",qnode.vertex, qnode.state, qnode.previousPath
        # prepare the visited hash, just coz you dont want if key else statement there
        visited = {vertex:[] for vertex in range(len(graph))}
        # put the origin vertex and state in visited hash
        visited[originVertex].append(qnode.state)
        print "The visited hash looks like this", visited
        while(queue):
            print "\nQueue so far",[[node.vertex, node.state] for node in queue]
            top = queue.pop(0)
            print "Top node is", top.vertex, 'its state is', top.state, 'previous path taken to reach this node ->',top.previousPath
            # since we are going to visit the top vertex, lets change the state.
            new_state = self.turnOnNthBitOfState(top.state, top.vertex)
            print "New state after visiting top vertex is", new_state
            if(new_state == '1'*len(graph)):
                print "We found the shortest path from origin vertex",originVertex
                print top.previousPath
                return
            for vertex in range(len(graph)):
                if(vertex == top.vertex):
                    continue
                print "Currently considering the vertex", vertex, 'to visit from our top node',top.vertex
                # we need to make sure that
                # there is an edge between current vertex and top vertex,
                if not(self.edgeBetweenVertex1andVertex2(graph, top.vertex, vertex)):
                    print "Oops there is not edge between top vertex", top.vertex, "and the current vertex",vertex
                    continue
                print "The visited state of vertex so far is", visited[vertex]
                # this new vertex we are going to put in queue and visit in future, we dont visit it with same 'state', you will understand this when you look at output.
                if(not(new_state in visited[vertex])):
                    visited[vertex].append(new_state)
                    print "The visited states of vertex after appending new state", visited[vertex]
                    node = self.createQNode(vertex, new_state)
                    node.previousPath = top.previousPath + node.previousPath
                    queue.append(node)
                else:
                    print "As you can see we have visited vertex",vertex,"in state",new_state,"before",
                    print "and we dont wanna visit it again"
            
        
        
    def shortestPathLength(self, graph):
        self.bfs(graph, 0)
        print "Now instead of selecting the origin vertex, you run this with every vertex and see which origin vertex gives you the min path"
        """
        :type graph: List[List[int]]
        :rtype: int
        """

# Main
obj = Solution()
obj.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])
