'''
https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 or l2
        val1,val2=[l1.val],[l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1=l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2=l2.next

        num1=''.join([str(i) for i in val1[::-1]])
        num2=''.join([str(i) for i in val2[::-1]])

        temp=str(int(num1)+int(num2))[::-1]
        res=ListNode(int(temp[0]))
        run_res=res
        for i in range(1,len(temp)):
            run_res.next=ListNode(int(temp[i]))
            run_res=run_res.next
        return res

# Recursive
class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 or l2
        else:
            if l1.val+l2.val<10:
                l3=ListNode(l1.val+l2.val)
                l3.next=self.addTwoNumbers(l1.next,l2.next)
            else:
                l3=ListNode(l1.val+l2.val-10)
                l3.next=self.addTwoNumbers(l1.next,self.addTwoNumbers(l2.next,ListNode(1)))
        return l3

# code testing
import json

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

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


l1 = stringToListNode('[2,4,3]')
l2 = stringToListNode('[5,6,4]')
print(listNodeToString(Solution().addTwoNumbers(l1, l2)))

