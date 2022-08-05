# Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    # produces level order traversal with each node value followed by number of children it has.
    # so for example it produces 1,4... because node with value 1 has 4 children
    def levelOrder(self, root):
        queue = [root]
        answer = ''
        while queue:
            top = queue.pop(0)
            answer += str(top.val) + ","
            answer += str(len(top.children)) + ","
            #print answer
            # add children
            for c in top.children:
                queue.append(c)
        # remove the comma at the end.
        return answer[:-1]
        
    def serialize(self, root):
        if not root:
            return []
        return self.levelOrder(root)
    
    def createNode(self, val, numChildren):
        node = Node()
        node.val = val
        node.children = [None for i in range(numChildren)]
        return node
    
    def deserialize(self, data):
        if not data:
            return 
        dataQ = data.split(',')
        # create a dummy root node
        root = self.createNode('root', 1)
        # add dummy root node to queue
        queue = [root]
        while(queue):
            topNode = queue.pop(0)
            # remove children from data
            for i in range(len(topNode.children)):
                # remove value of the node from data queue
                val = dataQ.pop(0)
                # the data queue has value of node followed by number of children it has, remove that from data queue.
                numChild = dataQ.pop(0)
                # create node for this val
                childNode = self.createNode(val, int(numChild))
                # attach this child node to topNode
                topNode.children[i] = childNode
                # add childNode in queue
                queue.append(childNode)
        # return node after root
        return root.children[0]
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
