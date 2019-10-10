'''
https://leetcode.com/problems/regular-expression-matching/
10. Regular Expression Matching
Hard

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        result[0][0]=True
        for i in range(1,len(p)):
            if p[i]=='*':
                result[0][i+1]=result[0][i-1]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]!='*':
                    result[i+1][j+1]=result[i][j] and (s[i]==p[j] or p[j]=='.')
                else:
                    result[i+1][j+1]=result[i+1][j-1] or result[i][j+1] and (s[i]==p[j-1] or p[j-1]=='.')
        return result[len(s)][len(p)]


class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        if len(p)==1 or p[1]!='*':
            if len(s)>0 and (p[0]==s[0] or p[0]=='.'):
                return self.isMatch(s[1:],p[1:])
            else:
                return False
        else:
            while len(s)>0 and (p[0]==s[0] or p[0]=='.'):
                if self.isMatch(s,p[2:]):
                    return True
                s=s[1:]
            return self.isMatch(s,p[2:])


print(Solution().isMatch('aa','a'))
print(Solution().isMatch('aa','a*'))
print(Solution().isMatch('aaa','ab*ac*a*'))
print(Solution().isMatch('ab','.*'))
print(Solution().isMatch('aab','c*a*b'))
print(Solution().isMatch('mississippi','mis*is*p*.'))
