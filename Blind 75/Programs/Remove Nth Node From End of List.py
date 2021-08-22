# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # we assign fast pointer rabbit to head
        rabbit = head
        # since head node is counted as 1, we stop when n = 1
        while(n > 1):
            # we want to advance rabbit to n nodes
            rabbit = rabbit.next
            n = n-1
        # we assign slow pointer tortoise to head
        tortoise = head
        # we also need previous pointer to concatinate the singly linked list
        prevPtr = head
        # move both rabbit and tortoise unitl rabbit reaches the end
        while(rabbit.next):
            prevPtr = tortoise
            rabbit = rabbit.next
            tortoise = tortoise.next
        # now tortoise is at the n th to last node.
        # if we have to remove head, just advance the head to it's next value, even if that value is null.
        if (tortoise == head):
            head = head.next
        else:
            # we remove tortoise with help of prev pointer
            prevPtr.next = tortoise.next
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
