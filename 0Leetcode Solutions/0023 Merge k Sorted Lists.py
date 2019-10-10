'''
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
Accepted
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            dummy = head = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            head.next = l1 or l2
            return dummy.next
        if not lists:
            return None
        left,right=0,len(lists)-1
        while right>0:
            if left>=right:
                left=0
            else:
                lists[left]=mergeTwoLists(lists[left],lists[right])
                left+=1
                right-=1
        return lists[0]

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes=[]
        head=point=ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l=l.next
        for i in sorted(nodes):
            point.next=ListNode(i)
            point=point.next
        return head.next


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


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


a=stringToListNodeArray('[[1,4,5],[1,3,4],[1,2,6]]')
print(listNodeToString(Solution1().mergeKLists(a)))