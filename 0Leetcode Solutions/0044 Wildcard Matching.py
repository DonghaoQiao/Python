'''
https://leetcode.com/problems/wildcard-matching/
44. Wildcard Matching
Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i,j,star,i_index=0,0,-1,0
        while i<len(s):
            if j<len(p) and (p[j]=='?' or p[j]==s[i]):
                i+=1
                j+=1
            elif j<len(p) and p[j]=='*':
                star=j
                j+=1
                i_index=i
            elif star!=-1:
                j=star+1
                i_index+=1
                i=i_index
            else:
                return False
        # while j<len(p) and p[j]=='*':
        #     j+=1
        return j==len(p)

print(Solution().isMatch('aa','a'))
print(Solution().isMatch('aa','*'))
print(Solution().isMatch('abcde','a*e'))
print(Solution().isMatch('abcde','a*b'))
print(Solution().isMatch('abcde','a??d?'))

print(Solution().isMatch('abcedce','a*e'))