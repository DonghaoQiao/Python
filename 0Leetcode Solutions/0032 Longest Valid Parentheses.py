'''
https://leetcode.com/problems/longest-valid-parentheses/
32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        dp=[0 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]==')':
                j=i-1-dp[i-1]
                if j>=0 and s[j]=='(':
                    dp[i]=dp[i-1]+2
                    if j-1>=0:
                        dp[i]+=dp[j-1]
        return max(dp)


print(Solution().longestValidParentheses('(()'))
print(Solution().longestValidParentheses(')()())'))
print(Solution().longestValidParentheses(')()(()))'))
print(Solution().longestValidParentheses('())()'))