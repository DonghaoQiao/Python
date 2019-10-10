'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited=[-1 for i in range(256)]
        index,longest=-1,0

        for i,char in enumerate(s):
            if visited[ord(char)]>index:
                index=visited[ord(char)]
            longest=max(longest,i-index)
            visited[ord(char)]=i
        return longest

class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, longest=0,0
        visited=[0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]==0:
                visited[ord(char)] = 1
            else:
                while char != s[start]:
                    visited[ord(s[start])]=0
                    start+=1
                start+=1

            longest=max(longest,i-start+1)
        return longest

# code testing
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('abcd'))
print(Solution().lengthOfLongestSubstring('abba'))

print()
print(Solution1().lengthOfLongestSubstring('abcabcbb'))
print(Solution1().lengthOfLongestSubstring('bbbbb'))
print(Solution1().lengthOfLongestSubstring('abcd'))
print(Solution1().lengthOfLongestSubstring('abba'))


