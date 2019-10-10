'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
33. Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        if left<=right:
            if target>=nums[left]:
                for i in range(len(nums)):
                    if nums[i]==target:
                        return i
            if target<=nums[right]:
                for i in range(len(nums)-1,0,-1):
                    if nums[i]==target:
                        return i
        return -1

class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                left+=1
        return -1


print(Solution1().search([4,5,6,7,0,1,2],0))
print(Solution1().search([4,5,6,7,0,1,2],3))
print(Solution1().search([1],1))
print(Solution1().search([],3))