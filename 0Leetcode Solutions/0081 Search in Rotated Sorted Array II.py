'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
81. Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''


class Solution(object):
    def search(self, nums, target):
        left,right=0,len(nums)-1
        if left<=right:
            if target>=nums[left]:
                for i in range(len(nums)):
                    if nums[i]==target:
                        return True
            if target<=nums[right]:
                for i in range(len(nums)-1,0,-1):
                    if nums[i]==target:
                        return i
        return False

class Solution1():
    def search(self, nums, target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return True
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
        return False


print(Solution1().search([2,5,6,0,0,1,2],0))
print(Solution1().search([2,5,6,0,0,1,2],3))
print(Solution1().search([1],1))
print(Solution1().search([],3))