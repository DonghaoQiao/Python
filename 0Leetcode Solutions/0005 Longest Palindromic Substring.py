'''
https://leetcode.com/problems/longest-palindromic-substring/
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

# 最慢最慢最简单
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxL=0
        start,end=0,0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and s[i:j+1]==s[i:j+1][::-1]:
                    if len(s[i:j+1])>maxL:
                        maxL=len(s[i:j+1])
                        start,end=i,j
        return s[start:end+1]

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<=1 or s==s[::-1]: return s

        start,longest=0,1
        for i in range(n):
            # 奇数个对称
            if i-longest>=1 and s[i-longest-1:i+1]==s[i-longest-1:i+1][::-1]:
                start=i-longest-1
                longest+=2
                continue
            # 偶数个对称
            if i-longest>=0 and s[i-longest:i+1]==s[i-longest:i+1][::-1]:
                start=i-longest
                longest+=1
        return s[start:start+longest]

class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<=1: return s
        start,longest=0,1
        substring=s[0]
        while start<n:
            i=start+1
            while i<n:
                if s[start]==s[i]: i+=1
                else: break
            k=0
            while start-k-1>=0 and i+k<=n-1:
                if s[start-k-1]!=s[i+k]:
                    break
                k+=1
            if i-start+2*k>longest:
                longest=i-start+2*k
                substring=s[start-k:i+k]
            if i+k==n-1:
                break
            start=i
        return substring


# 慢
class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i)
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome

class Solution4(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1: return s
        start,end=0,0
        maxL,n=0,len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i]=(s[j]==s[i])&((i-j<2)|dp[j+1][i-1])
                if dp[j][i] and maxL<i-j+1:
                    maxL=i-j+1
                    start=j
                    end=i
            dp[i][i]=1
        return s[start:end+1]

print(Solution4().longestPalindrome('babad'))
print(Solution4().longestPalindrome('cbbd'))
print(Solution4().longestPalindrome('ccc'))