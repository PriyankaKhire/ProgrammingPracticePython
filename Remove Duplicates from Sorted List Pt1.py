# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def traverseLinkedList(self, prevNode, currNode):
        if (currNode == None):
            return
        # remove current node
        if (prevNode and prevNode.val == currNode.val):
            prevNode.next = currNode.next
            # garbage collection
            currNode.next = None
            self.traverseLinkedList(prevNode, prevNode.next)
        else:
            self.traverseLinkedList(currNode, currNode.next)
        
    def deleteDuplicates(self, head):
        self.traverseLinkedList(None, head)
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
