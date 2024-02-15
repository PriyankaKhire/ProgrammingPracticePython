# Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def attachChildToParent(self, parent, child, node):
        if (parent.left == node):
            parent.left = child
            return
        parent.right = child

    def preOrder(self, parent, node, low, high):
        if not node:
            return
        print "Node value", node.val
        # if current node is lower than low we can throw away its entire left sub tree.
        if (node.val < low):
            # print "Node value lower than low"
            # attach the child to parent
            if parent:
                self.attachChildToParent(parent, node.right, node)
            if (node.right != None):
                # then go in that sub tree to find more
                self.preOrder(parent, node.right, low, high)
        elif (node.val > high):
            print "Node value higher than high"
            # throw away the entire right sub tree
            # attach child to parent
            if parent:
                self.attachChildToParent(parent, node.left, node)
            if (node.left != None):
                # then go in that sub tree to find more
                self.preOrder(parent, node.left, low, high)
        else:
            # otherwise if the node value lies exactly in the middle then go dee in the tree
            # print "going left"
            self.preOrder(node, node.left, low, high)
            # print "going right"
            self.preOrder(node, node.right, low, high)

    def trimBST(self, root, low, high):
        if ((root.val < low or root.val > high) and (root.left == None and root.right == None)):
            return
        if (root.val < low and root.right != None):
            root = root.right
        elif (root.val > high and root.left != None):
            root = root.left
        self.preOrder(None, root, low, high)
        return root
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
