'''
https://leetcode.com/problems/combination-sum/
39. Combination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(candidates,target,current,result):
            if target==0:
                result.append(current)
                return
            if current and target<current[-1]:
                return
            for i,v in enumerate(candidates):
                combination(candidates[i:],target-candidates[i],current+[v],result)
        result=list()
        candidates.sort()
        combination(candidates,target,list(),result)
        return result

class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combination(candidates,target,current,result):
            s=sum(current) if current else 0
            if s>target:
                return
            elif s==target:
                result.append(current)
            else:
                for i,v in enumerate(candidates):
                    combination(candidates[i:],target,current+[v],result)
        if not candidates: return []
        candidates.sort()
        result=[]
        combination(candidates,target,[],result)
        return result

print(Solution().combinationSum([2,3,6,7],7))
print(Solution().combinationSum([2,3,5],8))