# Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""


class Codec:
    def preOrder(self, node, string):
        if not node:
            return
        # add the value of the node to string
        string[0] += "," + str(node.val)
        # go to the kids
        for c in node.children:
            self.preOrder(c, string)
            # add bracket for backtracking
            string[0] += ")"

    def serialize(self, root):
        string = [""]
        self.preOrder(root, string)
        return string[0][1:]
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

    def deserialize(self, data):
        if not data:
            return
        dataList = data.split(",")
        stack = []
        for char in dataList:
            nodeArray = char.split(")")
            for element in nodeArray:
                if (element != ''):
                    # print "Adding element ", element
                    # create a node and add as child of top stack element and put it back in stack
                    node = Node(int(element))
                    if (stack):
                        top = stack[-1]
                        # print "top of stack is", top.val
                        top.children.append(node)
                    stack.append(node)
                    # print "Adding element to stack", node.val
                    continue
                # else pop the stack element
                popNode = stack.pop()
                # print "Popped node", popNode.val
        return stack[0]
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))