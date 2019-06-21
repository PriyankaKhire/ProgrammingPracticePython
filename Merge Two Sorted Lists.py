# Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if (not l1 and not l2):
            return
        if(l1 and not l2):
            return l1
        if(l2 and not l1):
            return l2
        l3 = None
        if(l1.val <= l2.val):
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
        ptr3 = l3
        while(l1 and l2):
            if(l1.val <= l2.val):
                ptr3.next = l1
                l1 = l1.next
            else:
                ptr3.next = l2
                l2 = l2.next
            ptr3 = ptr3.next
        if(l1):
            ptr3.next = l1
        if(l2):
            ptr3.next = l2
        return l3
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
