"""
https://leetcode.com/problems/reverse-nodes-in-k-group/description/
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

def reverse(head: ListNode) -> ListNode :
    result = None
    while head:
        temp = result
        result = ListNode(head.val)
        result.next = temp
        head = head.next
    return result

def toList(head: ListNode)-> [int]:
    result = []
    while head:
        result.append(head.val)
        head=head.next
    return result

def toListNode(ls: [int])-> ListNode:
    result = None
    for x in ls[::-1]:
        temp = result
        result= ListNode(x)
        result.next = temp
    return result
def print_ln(ln: ListNode):print(toList(ln))

def reverseK(head: ListNode, K : int)-> ListNode:
    result = None
    i = 0
    segment = None
    result = None
    newHead = None
    while head:
        if i < K :
            temp = segment
            segment = ListNode(head.val)
            if not newHead : newHead = segment
            segment.next=temp
            head = head.next
            i+=1
        else:
            if not result: result = segment
            # newHead.next = segment
            segment = newHead
            newHead = None
            i = 0

    return result


#print
# ln = toListNode([1,2,3])
#
# ls = toList(ln)
#
#
#
# rv = reverse(ln)
# print_ln(rv)
ls = list(range(0,10))
ln = toListNode(ls)

reversedK = reverseK(ln, 3)
print(toList(reversedK))