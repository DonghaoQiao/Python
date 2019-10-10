'''
https://leetcode.com/problems/remove-linked-list-elements/
203. Remove Linked List Elements
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next

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


print(listNodeToString(Solution().removeElements(stringToListNode('[1,2,6,3,4,5,6]'),6)))
