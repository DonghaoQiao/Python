'''
https://leetcode.com/problems/4sum/
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]: continue
                left,right=j+1,len(nums)-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total<target:
                        left+=1
                    elif total>target:
                        right-=1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
        return result


print(Solution().fourSum([1, 0, -1, 0, -2, 2],0))
print(Solution().fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2],-9))
