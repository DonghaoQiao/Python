'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]

        left,right=0,len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target and (mid==0 or nums[mid-1]!=target):
                result.append(mid)
                break
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if not result:
            return [-1,-1]

        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]!=target):
                result.append(mid)
                break
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid
        return result


print(Solution().searchRange([5,7,7,8,8,10],8))
print(Solution().searchRange([5,7,7,8,8,10],6))