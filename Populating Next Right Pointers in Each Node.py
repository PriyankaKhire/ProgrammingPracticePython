# Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def preOrder(self, node):
        if node:
            # set the left pointer
            if(node.left != None):
                node.left.next = node.right
            # set the right pointer
            if(node.right != None and node.next != None):
                node.right.next = node.next.left
            # traverse left
            self.preOrder(node.left)
            # traverse right
            self.preOrder(node.right)
            
    def connect(self, root):
        self.preOrder(root)
        return root
        """
        :type root: Node
        :rtype: Node
        """
