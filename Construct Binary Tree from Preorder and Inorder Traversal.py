# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def preInOrder(self, preorder, inorder):
        print "preorder", preorder, "inorder", inorder
        if not inorder:
            print "returning none"
            return
        if (len(inorder) == 1):
            # pop the leaf from preorder
            preorder.pop(0)
            print "returning the leaf"
            # create a node and return
            return TreeNode(inorder[0])
        root = preorder.pop(0)
        # find index of root in inorder
        index = inorder.index(root)
        # split into left sub tree and right sub tree
        left = inorder[:index]
        right = inorder[index+1:]
        leftChild = self.preInOrder(preorder, left)
        rightChild = self.preInOrder(preorder, right)
        # create node and attach left and right child
        node = TreeNode(root)
        print "Creating node for", root
        node.left = leftChild
        node.right = rightChild
        return node
    
    def buildTree(self, preorder, inorder):
        return self.preInOrder(preorder, inorder)
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
