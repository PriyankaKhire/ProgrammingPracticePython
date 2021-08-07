# Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrderTraversal(self, node):
        if not node:
            return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        # swap kids
        rightChild = node.right
        leftChild = node.left
        node.right = leftChild
        node.left = rightChild
            
    def invertTree(self, root):
        self.postOrderTraversal(root)
        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
