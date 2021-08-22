# Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Get total sum by simple inorder traversal.
    def totalSum(self, node, currSum):
        if not node:
            return
        self.totalSum(node.left, currSum)
        currSum[0] = currSum[0]+node.val
        self.totalSum(node.right, currSum)
    
    # This function is very similar to findig height of tree.
    def maxSum(self, node, currMaxSum, totalSum):
        # If there is no node, we return zero since this zero will get added to leaf sub tree sum.
        if not node:
            return 0
        # Get left sub tree sum
        leftSubTreeSum = self.maxSum(node.left, currMaxSum, totalSum)
        # Get right sub tree sum.
        rightSubTreeSum = self.maxSum(node.right, currMaxSum, totalSum)
        # Calculate sum of current sub tree.
        currentSubTreeSum = leftSubTreeSum+rightSubTreeSum+node.val
        # Calculate the current max
        currMaxSum[0] = max(currMaxSum[0], (totalSum-currentSubTreeSum)*currentSubTreeSum)
        # Return the sum of current sub tree.
        return currentSubTreeSum
        
    def maxProduct(self, root):
        # Get the total sum of the tree.
        totalSumOfTree = [0]
        self.totalSum(root, totalSumOfTree)
        # Calculate the sub tree sum and get max.
        currMaxSum = [0]
        self.maxSum(root, currMaxSum, totalSumOfTree[0])
        # Since we need the answer modulo 10^9 + 7 (Leetcode requirement)
        return currMaxSum[0] % 1000000007
        """
        :type root: TreeNode
        :rtype: int
        """
        
