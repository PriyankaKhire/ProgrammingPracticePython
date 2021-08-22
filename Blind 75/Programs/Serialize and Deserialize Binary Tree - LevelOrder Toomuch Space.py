# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def height(self, node):
        if not node:
            return 0
        leftSubTreeHeight = self.height(node.left)
        rightSubTreeHeight = self.height(node.right)
        return max(leftSubTreeHeight, rightSubTreeHeight) + 1
    
    def totalNodes(self, height):
        nodeCount = 0
        for i in range(height):
            # at every depth the tree has 2^depth number of nodes
            nodeCount = nodeCount + pow(2, i)
        return nodeCount
    
    def inOrder(self, node, cellIndex, array):
        if not node:
            return
        # the left node cells are at 2n+1
        self.inOrder(node.left, (2*cellIndex)+1, array)
        # fill the array
        if (cellIndex < len(array)):
            # We later need to join it and return it as a string
            array[cellIndex] = str(node.val)
        # the right node cells are at 2n+2
        self.inOrder(node.right, (2*cellIndex)+2, array)
        
    def serialize(self, root):
        treeHeight = self.height(root)
        # calculate total number of nodes in complete binary tree
        totalNodes = self.totalNodes(treeHeight)
        # take an array and assign those many empty spaces
        allNodes = ["Null" for i in range(totalNodes)]
        # fill the nodes, any traversal will work here
        self.inOrder(root, 0, allNodes)
        return ','.join(allNodes)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    def createNode(self, val):
        return TreeNode(int(val))
    
    def createTree(self, node, array, index):
        # if the current node index doesn't have any kids and is out of bounds of the array
        if ((2*index)+1 > len(array)-1):
            return
        # add left subtree, the vaue of left node is located at 2n+1 in array
        leftValue = array[(2*index)+1]
        if (leftValue != "Null"):
            node.left = self.createNode(leftValue)
            # go left
            self.createTree(node.left, array, (2*index)+1)
        # add right subtree, the vaue of right node is located at 2n+2 in array
        rightValue = array[(2*index)+2]
        if (rightValue != "Null"):
            node.right = self.createNode(rightValue)
            # go right
            self.createTree(node.right, array, (2*index)+2)
        

    def deserialize(self, data):
        if not data:
            return []
        # split data with help of comma as delimiter.
        nodeList = data.split(",")
        # create root
        root = self.createNode(nodeList[0])
        print nodeList
        self.createTree(root, nodeList, 0)
        return root
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
