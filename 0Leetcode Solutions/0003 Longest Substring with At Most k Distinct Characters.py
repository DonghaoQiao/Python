'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example,
Given s = “eceba”,
T is "ece" which its length is 3.
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k==0:
            return 0
        j,longest,score=0,0,0
        substring={}
        for i in range(len(s)):
            while j<len(s) and (score<k or substring.get(s[j],0)!=0):
                if substring.get(s[j],0)==0:
                    score+=1
                substring[s[j]]=substring.get(s[j],0)+1
                j+=1
            longest=max(longest,j-i)
            substring[s[i]]-=1
            if substring[s[i]]==0:
                score-=1
        return longest

class Solution1:
    def lengthOfLongestSubstring(self, s):
        start, longest=0,0
        visited=[False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])]=False
                    start+=1
                start+=1
            else:
                visited[ord(char)]=True
            longest=max(longest,i-start+1)
        return longest

    def lengthOfLongestSubstringKDistinct(self, s, k):
        start, longest, count=0, 0, 0
        visited=[0 for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]==0:
                count+=1
            visited[ord(char)]+=1
            while count>k:
                visited[ord(s[start])]-=1
                if visited[ord(s[start])]==0:
                    count-=1
                start+=1
            longest=max(longest,i-start+1)
        return longest






print(Solution1().lengthOfLongestSubstringKDistinct('abcbadc',3))
''
print(Solution1().lengthOfLongestSubstringKDistinct('bbbbb',2))
print(Solution1().lengthOfLongestSubstringKDistinct('eceba',2))