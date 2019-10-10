'''
https://leetcode.com/problems/3sum-closest/
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that
the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result=min_diff=float('inf')
        for i in range(len(nums)-1):
            if i == 0 or nums[i] == nums[i - 1]:
                left,right=i+1,len(nums)-1
                while left<right:
                    diff=nums[i]+nums[left]+nums[right]-target
                    if abs(diff)<min_diff:
                        min_diff=abs(diff)
                        result=nums[i]+nums[left]+nums[right]
                    if diff<0: left+=1
                    elif diff>0: right-=1
                    else: return target
        return result

print(Solution().threeSumClosest([-1, 2, 1, -4],1))
print(Solution().threeSumClosest([0,1,2],3))
