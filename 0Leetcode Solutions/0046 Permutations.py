'''
https://leetcode.com/problems/permutations/
46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteRec(nums, current, result):
            if not nums:
                result.append(current[:])
                return
            for i in range(len(nums)):
                current.append(nums[i])
                permuteRec(nums[:i]+nums[i+1:],current,result)
                current.pop()
        current,result=[],[]
        permuteRec(nums,current,result)
        return result

class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteRec(nums,i):
            if i==len(nums)-1:
                result.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                permuteRec(nums[:],i+1)
        result=[]
        permuteRec(nums,0)
        return result

print(Solution1().permute([1,2,3]))