'''
https://leetcode.com/problems/two-sum/
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen.keys():
                return [seen[nums[i]],i]
            else:
                seen[target-nums[i]]=i

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            sub = target-num
            if sub in nums:
                if i != nums.index(sub):
                    return [i, nums.index(sub)]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            sub = target-num
            if sub in seen:
                return [seen[sub], i]
            seen[num] = i
        return []


print(Solution1().twoSum([2, 7, 11, 15], 9))
print(Solution1().twoSum([3, 2, 4], 6))

print(Solution2().twoSum([2, 7, 11, 15], 9))
print(Solution2().twoSum([3, 2, 4], 6))
