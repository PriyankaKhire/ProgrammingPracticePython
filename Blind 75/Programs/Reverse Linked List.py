# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # If head is empty
        if not head:
            return
        # If there are only 2 nodes
        if not head.next:
            return head
        # Assign 3 pointers
        prevPtr = head
        currPtr = head
        nextPtr = head.next
        # Change direction of all nexts.
        while(nextPtr):
            print currPtr.val
            currPtr = nextPtr
            nextPtr = nextPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
        # Finally assign our first pointer next to None, to avoid cycle.
        head.next = None
        return currPtr
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
