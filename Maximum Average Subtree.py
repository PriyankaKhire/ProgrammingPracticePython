# Maximum Average Subtree
# https://leetcode.com/problems/maximum-average-subtree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrder(self, node, maxAvg):
        if not node:
            return 0, 0
        left, nodesOnLeft = self.postOrder(node.left, maxAvg)
        right, nodesOnRight = self.postOrder(node.right, maxAvg)
        avg = (node.val + left + right)/float(1+ nodesOnLeft + nodesOnRight)
        # update the maximum average
        maxAvg[0] = max(avg, maxAvg[0])
        #return sum
        return node.val + left + right, 1+ nodesOnLeft + nodesOnRight


    def maximumAverageSubtree(self, root):
        maxAvg = [0]
        self.postOrder(root, maxAvg)
        return maxAvg[0]
        """
        :type root: TreeNode
        :rtype: float
        """
        
