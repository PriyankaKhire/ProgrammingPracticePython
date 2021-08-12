# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return
        # tortoise that moves 1 space at a time
        tortoise = head
        # rabbit that moves 2 spaces at a time.
        rabbit = head
        # While rabbit can still move
        while(rabbit.next):
            tortoise = tortoise.next
            rabbit = rabbit.next
            # if rabbit cannot move 2 spaces then there is no cycle and we come out of while loop.
            if not rabbit.next:
                break
            rabbit = rabbit.next
            # if at any given point, rabbit and tortoise meet then there is a cycle.
            if (rabbit == tortoise):
                return True
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        
