#BFS
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = Node("root")
        self.createTree()

    def createNode(self, val):
        return Node(val)

    def createTree(self):
        self.root.left = Node(1)
        self.root.right = Node(2)
        self.root.left.left = Node(3)
        self.root.left.right = Node(4)
        self.root.right.left = Node(5)
        self.root.right.right = Node(6)
    '''
       root
     1      2
    3 4   5 6
    '''

class Graph(object):
    def __init__(self):
        self.matrix = []
        self.createGraph()

    '''
                            ______D
      _____B           /
     |          ______C----------E------
    A         |          \                         |
    |______S           |_________F         |
              |                           |         |
              ---------G--------/         |
                            |                      |
                            ---------------H
    '''
    def createGraph(self):
        self.matrix = [[0 for col in range(9)] for row in range(9)]
        self.matrix[0][1] = 1
        self.matrix[0][8] = 1
        self.matrix[1][0] = 1
        self.matrix[8][0] = 1
        self.matrix[8][2] = 1
        self.matrix[8][6] = 1
        self.matrix[2][8] = 1
        self.matrix[2][3] = 1
        self.matrix[2][4] = 1
        self.matrix[2][5] = 1
        self.matrix[3][2] = 1
        self.matrix[4][2] = 1
        self.matrix[4][7] = 1
        self.matrix[5][2] = 1
        self.matrix[5][6] = 1
        self.matrix[6][8] = 1
        self.matrix[6][5] = 1
        self.matrix[6][7] = 1
        self.matrix[7][6] = 1
        self.matrix[7][4] = 1

class BFS(object):
    
    def levelOrder(self, node):
        queue = [[node, 0]]
        visited = []
        while queue:
            [currentlyWorkingNode, level] = queue.pop(0)
            #mark the current node visited
            visited.append([currentlyWorkingNode.val, level])
            # put all it's children in queue
            if (currentlyWorkingNode.left):
                queue.append([currentlyWorkingNode.left, level+1])
            if (currentlyWorkingNode.right):
                queue.append([currentlyWorkingNode.right, level+1])
        # print the nodes
        l = 0
        for node, level in visited:
            if (level == l):
                print node,
            else:
                l = level
                print "\n",node,
        print "\n"
            
    def treeTraversal(self):
        print "Tree Traversal"
        tree = Tree()
        self.levelOrder(tree.root)

    def iterative(self, matrix):
        # since we know there are no isolated nodes in this graph
        # if there were we would have used a for loop to check if all nodes are visited or not
        queue = [0]
        visited = []
        while(queue):
            top = queue.pop(0)
            # mark the node visited
            visited.append(top)
            # add all children to queue
            for child in range(len(matrix)):
                if ((child not in queue) and (child not in visited) and matrix[top][child] == 1):
                    queue.append(child)
        print visited

    def graphTraversal(self):
        print "\nGraph traversal"
        graph = Graph()
        self.iterative(graph.matrix)

# Main
obj = BFS()
obj.treeTraversal()
obj.graphTraversal()
        
