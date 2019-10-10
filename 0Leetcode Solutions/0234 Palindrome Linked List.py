'''
https://leetcode.com/problems/palindrome-linked-list/
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def isPalindrome(self,head):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        return l==l[::-1]


class Solution1():
    def isPalindrome(self, head):
        reverse,temp=None,head
        # reverse the first part of the list
        while temp and temp.next:
            temp=temp.next.next
            head.next,reverse,head=reverse,head,head.next
        # If the number of the nodes is odd, set the head of the
        # tail list to the next of the median node
        tail=head.next if temp else head

        result=True
        while reverse:
            result=result and reverse.val==tail.val
            reverse.next,head,reverse=head,reverse,reverse.next
            tail=tail.next

        return result


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


print(Solution1().isPalindrome(stringToListNode('[1,2]')))
print(Solution1().isPalindrome(stringToListNode('[1,2,2,1]')))


