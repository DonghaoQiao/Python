'''
https://leetcode.com/problems/combination-sum-ii/
40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if i>0 and candidates[i]==candidates[i-1]:
                    continue
                combination(candidates[i+1:],target-candidates[i],current+[v],result)
        result=list()
        candidates.sort()
        combination(candidates,target,list(),result)
        return result

print(Solution().combinationSum2([10,1,2,7,6,1,5],8))