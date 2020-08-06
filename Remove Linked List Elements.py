# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeVal(self, prev, node):
        if(prev == node):
            return node.next
        prev.next = node.next
        return prev
        
    def removeElements(self, head, val):
        # if linked list empty
        if not head:
            return
        # inital case to remove head
        while(head and head.val == val):
            head = head.next
        ptr = head
        prev = ptr
        while(ptr != None):
            if(ptr.val == val):
                ptr = self.removeVal(prev, ptr)
            prev = ptr
            ptr = ptr.next
        return head
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
