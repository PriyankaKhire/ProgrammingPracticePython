# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def preOrder(self, node, output):
        if not node:
            output.append("#")
            return
        output.append(str(node.val))
        self.preOrder(node.left, output)
        self.preOrder(node.right, output)

    def serialize(self, root):
        output = []
        self.preOrder(root, output)
        return ",".join(output)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
    
    def createNode(self, data):
        return TreeNode(data)
    
    def constructPreOrder(self, data):
        #print data
        if(not data):
            return
        if(data[0] == "#"):
            data.pop(0)
            return
        node = self.createNode(data[0])
        data.pop(0)
        node.left = self.constructPreOrder(data)
        node.right = self.constructPreOrder(data)
        return node
    
    def deserialize(self, data):
        return self.constructPreOrder(data.split(","))
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
