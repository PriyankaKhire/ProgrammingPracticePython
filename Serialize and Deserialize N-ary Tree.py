# Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    
    def preOrder(self, node, string):
        if not node:
            return
        string[0] = string[0] + str(node.val) + ","
        if not(node.children):
            return
        string[0] = string[0] +  "["
        for n in node.children:
            self.preOrder(n, string)
        string[0] = string[0] + "]"

    def serialize(self, root):
        string = [""]
        self.preOrder(root, string)
        return string[0]
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        #Produces result like 1,[3,[5,6]2,4]
        # where 1 is root, 3,2,4 are childern of 1, and 5,6 are children of 3
        
    def createNode(self, val):
        return Node(int(val), [])

    def deserialize(self, data):
        if(data == ""):
            return
        print data
        root = None
        stack = []
        i = 0
        while(i < len(data)):
            if(data[i] == ']'):
                stack.pop()
                i = i+1
                continue
            number = ""
            while(data[i]!=","):
                number = number+data[i]
                i = i+1
            node = self.createNode(number)
            if(root == None):
                root = node
            else:
                stack[-1].children.append(node)
                print node.val,"as child of",stack[-1].val
            if(i+1 < len(data) and data[i+1] == '['):
                stack.append(node)
                i = i+1
            if(i+1 < len(data) and data[i+1] == ']'):
                stack.pop()
                i = i+1
            print [j.val for j in stack]
            i = i+1
        return root
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
