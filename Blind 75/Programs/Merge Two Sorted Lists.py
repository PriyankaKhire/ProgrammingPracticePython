# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # create an empty head for the list
        head = ListNode()
        # assign pointer to this head, this is to keep track.
        ptr = head
        # while both the lists are still alive.
        while(l1 and l2):
            if (l1.val < l2.val):
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        # add remaining of the lists
        if (l1):
            ptr.next = l1
        if (l2):
            ptr.next = l2
        # return the head next since head is empty pointer.
        return head.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
