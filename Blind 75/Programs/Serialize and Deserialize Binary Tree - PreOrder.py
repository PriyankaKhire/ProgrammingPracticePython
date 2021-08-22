# Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def preOrder(self, node, array):
        if not node:
            array.append("null")
            return
        array.append(str(node.val))
        self.preOrder(node.left, array)
        self.preOrder(node.right, array)
        
    def serialize(self, root):
        array = []
        self.preOrder(root, array)
        # Join the result using comma as delimiter.
        return ",".join(array)
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
    def createNode(self, val):
        return TreeNode(int(val))
    
    def preOrderCreateTree(self, array, index):
        # The reason why we use index as list and not a single number is because a single number gets modified within recurssive calls but a list does not.
        if (index[0] > len(array) or array[index[0]] == 'null'):
            return
        # Create the node with the value.
        node = self.createNode(array[index[0]])
        # Increment the index and get the left side of the node.
        index[0] = index[0] + 1
        node.left = self.preOrderCreateTree(array, index)
        # Increment the index and get the right side of the node.
        index[0] = index[0] + 1
        node.right = self.preOrderCreateTree(array, index)
        # Return this node, so it can be added to left or right of the calling parent.
        return node

    def deserialize(self, data):
        if not data:
            return []
        # Split the data into a list, using comma as delimiter.
        nodeList = data.split(",")
        # Create the tree.
        node = self.preOrderCreateTree(nodeList, [0])
        # Return the root of the tree.
        return node
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
