'''
https://leetcode.com/problems/3sum/
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0: break
            if i==0 or nums[i]!=nums[i-1]:
                left,right=i+1,len(nums)-1
                while left<right:
                    total=nums[i]+nums[left]+nums[right]
                    if total<0: left+=1
                    elif total>0: right-=1
                    else:
                        result.append([nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))