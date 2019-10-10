'''
https://leetcode.com/problems/permutations-ii/
47. Permutations II
Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteRec(nums,current,result):
            if not nums:
                result.append(current[:])
                return
            for i in range(len(nums)):
                if i-1>=0 and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                permuteRec(nums[:i]+nums[i+1:],current,result)
                current.pop()
        nums.sort()
        current,result=[],[]
        permuteRec(nums,current,result)
        return result

class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteRec(nums,i):
            if i==len(nums)-1:
                result.append(nums[:])
                return
            for j in range(i,len(nums)):
                if i!=j and nums[i]==nums[j]:
                    continue
                nums[i],nums[j]=nums[j],nums[i]
                permuteRec(nums[:],i+1)
        nums.sort()
        result=[]
        permuteRec(nums,0)
        return result


print(Solution1().permuteUnique([1,1,2]))