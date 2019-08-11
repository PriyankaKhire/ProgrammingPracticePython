# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.verticalPos = {}
    
    def addToHash(self, node, vertical, level):
        if not(vertical in self.verticalPos):
            self.verticalPos[vertical] = {level:[node]}
        else:
            if not(level in self.verticalPos[vertical]):
                self.verticalPos[vertical][level] = [node]
            else:
                self.verticalPos[vertical][level].append(node)
    
    def inorder(self, node, vp, level):
        if(node):
            self.inorder(node.left, vp-1, level+1)
            self.addToHash(node.val, vp, level)
            self.inorder(node.right, vp+1, level+1)
        
    def verticalTraversal(self, root):
        self.inorder(root, 0, 0)
        output = []
        for key in sorted(self.verticalPos):
            verticalLine = []
            for level in self.verticalPos[key]:
                verticalLine = verticalLine + sorted(self.verticalPos[key][level])
            print verticalLine
        return output
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
