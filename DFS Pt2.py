# DFS
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

class DFS(object):
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print node.val,
        self.inOrder(node.right)

    def preOrder(self,node):
        if not node:
            return
        print node.val,
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node):
        if not node:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print node.val,
        
    def treeTraversal(self):
        print "Tree Traversal"
        tree = Tree()
        print "Inorder traversal"
        self.inOrder(tree.root)
        print "\nPreOrder traversal"
        self.preOrder(tree.root)
        print "\nPostOrder traversal"
        self.postOrder(tree.root)

    def recursive(self, visited, matrix, topElement):
        if (len(visited) == len(matrix)):
            # The graph has been completely visited
            return
        # mark the top element as visited
        visited.append(topElement)
        # visit all the children of the top element
        for child in range(len(matrix)):
            if (matrix[topElement][child] == 1 and (child not in visited)):
                # visit the child
                self.recursive(visited, matrix, child)
        

    def graphTraversal(self):
        print "\nGraph Traversal"
        graph = Graph()
        matrix = graph.matrix
        # Here we will start with zero, since the whole graph is connected we don't need to put this in a for loop
        # but if the graph was not connected then we'd check for each element if it's been visited or not
        visited = []
        self.recursive(visited, matrix, 0)
        print visited
        
        
        

# Main
obj = DFS()
obj.treeTraversal()
obj.graphTraversal()
        
        
        
 
        
