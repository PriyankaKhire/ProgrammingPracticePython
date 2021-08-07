# Same Tree
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, node, values):
        if not node:
            # we need to append this so the traversal is true
            values.append(None)
            return
        self.inOrder(node.left, values)
        values.append(node.val)
        self.inOrder(node.right, values)
    
    def postOrder(self, node, values):
        if not node:
            # we need to append this so the traversal is true
            values.append(None)
            return
        self.postOrder(node.left, values)
        self.postOrder(node.right, values)
        values.append(node.val)
        
    def isSameTree(self, p, q):
        # do in-order traversal of the trees
        inOrderP = []
        self.inOrder(p, inOrderP)
        inOrderQ = []
        self.inOrder(q, inOrderQ)
        # do post-order traversal of the trees
        postOrderP = []
        self.postOrder(p, postOrderP)
        postOrderQ = []
        self.postOrder(q, postOrderQ)
        # compare
        if (inOrderP == inOrderQ and postOrderP == postOrderQ):
            return True
        return False
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
