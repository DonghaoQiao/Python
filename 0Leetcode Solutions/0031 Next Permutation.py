'''
https://leetcode.com/problems/next-permutation/
31. Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        target,temp=-1,0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                target=i
        if target==-1:
            nums.reverse()
            return
        for i in range(target+1,len(nums)):
            if nums[i]>nums[target]:
                temp=i
        nums[target],nums[temp]=nums[temp],nums[target]
        nums[target+1:]=reversed(nums[target+1:])


class Solution1(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        target=temp=0

        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                target=i-1
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[target]:
                temp=i
                break
        nums[target],nums[temp]=nums[temp],nums[target]
        if target==temp==0:
            nums.reverse()
        else:
            nums[target+1:]=reversed(nums[target+1:])


nums=[1,2,7,4,3]
Solution().nextPermutation(nums)
print(nums)

nums=[1,7,3]
Solution().nextPermutation(nums)
print(nums)