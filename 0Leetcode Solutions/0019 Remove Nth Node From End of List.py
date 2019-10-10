'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        fast=slow=dummy

        while n and fast:
            fast=fast.next
            n-=1
        while fast.next and slow.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next

class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head

        l=0
        pre=dummy
        while pre.next:
            l+=1
            pre=pre.next

        pre=dummy
        count=0
        while pre.next:
            cur=pre.next
            if count==l-n:
                pre.next=cur.next
                break
            else:
                count+=1
                pre=pre.next
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


print(listNodeToString(Solution().removeNthFromEnd(stringToListNode('[1,2,3,4,5]'),2)))
print(listNodeToString(Solution1().removeNthFromEnd(stringToListNode('[1,2,3,4,5]'),2)))

