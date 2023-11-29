# Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, node, values):
        if (node == None):
            return
        self.inOrder(node.left, values)
        values.append(node.val)
        self.inOrder(node.right, values)

    def inorderTraversal(self, root):
        values = []
        self.inOrder(root, values)
        return values
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
