'''
https://leetcode.com/problems/generate-parentheses/
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        self.dfs(result, '', n, n)
        return result
    def dfs(self, result, cur, left, right):
        if left==0 and right==0:
            result.append(cur)
            return
        # add left
        if left>0:
            self.dfs(result,cur+'(',left-1,right)
        if right>left:
            self.dfs(result,cur+')',left,right-1)
        print(result)

print(Solution().generateParenthesis(3))