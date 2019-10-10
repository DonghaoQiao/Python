'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        cur,cur_dummy=head,dummy
        length=0

        while cur:
            next_cur=cur.next
            length=(length+1)%k

            if length==0:
                next_dummy=cur_dummy.next
                self.reverse(cur_dummy,cur.next)
                cur_dummy=next_dummy
            cur=next_cur
        return dummy.next

    def reverse(self, begin,end):
        first=begin.next
        cur=first.next

        while cur!=end:
            first.next=cur.next
            cur.next=begin.next
            begin.next=cur
            cur=first.next


import json

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


print(listNodeToString(Solution().reverseKGroup(stringToListNode('[1,2,3,4,5,6,7,8]'),3)))

