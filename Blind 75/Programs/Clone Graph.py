# Clone Graph
# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        # key: value of node, Val: node
        self.nodesHash = {}
    
    def createCopyNode(self, val):
        # create the node and assign it value
        node = Node(val)
        # add the node to hash
        self.nodesHash[val] = node
    
    def dfs(self, node, visited):
        print "Currently visiting", node.val
        # visit the node
        visited.append(node)
        # create copy of the node
        self.createCopyNode(node.val)
        # get all it's neighbors
        for neighbor in node.neighbors:
            # if the neighbor is unvisited
            if not neighbor in visited:
                self.dfs(neighbor, visited)
    
    def bfs(self, visited, queue):
        if not queue:
            return
        # Get the top of the queue.
        topNode = queue.pop(0)
        print "queue top", topNode.val
        print "visited", [n.val for n in visited]
        # for all neighbors of the current node
        for neighbor in topNode.neighbors:
            print "neighbor", neighbor.val
            # add to queue
            if (neighbor not in visited):
                print "Adding to queue"
                queue.append(neighbor)
            # if the copy of this connection is not present in the copy node's neighbors then add it.
            if (self.nodesHash[neighbor.val] not in self.nodesHash[topNode.val].neighbors):
                self.nodesHash[topNode.val].neighbors.append(self.nodesHash[neighbor.val])
        # mark the node as visited
        visited.append(topNode)
        self.bfs(visited, queue)
        
        
    def cloneGraph(self, node):
        # edge case where graph is empty.
        if not node:
            return node
        # Get all the nodes and create a hash table out of it.
        # Note: you can also do this using bfs. I am just doing both for practice.
        self.dfs(node, [])
        # join the nodes
        self.bfs([], [node])
        return self.nodesHash[node.val]
        """
        :type node: Node
        :rtype: Node
        """
        
