"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tortoise = hare = head
        while n > 1 and hare:
            hare = hare.next
            n -=1
        while hare:
            hare = hare.next
            tortoise=tortoise.next
        if tortoise.next: tortoise.next = tortoise.next.next


        return head
