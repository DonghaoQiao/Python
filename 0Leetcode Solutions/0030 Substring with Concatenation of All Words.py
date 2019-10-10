'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
30. Substring with Concatenation of All Words
Hard

You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly
once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return
        s_length,word_length,word_num=len(s),len(words[0]),len(words)
        words_length=word_num*word_length
        result,words_dict=[],{}

        for word in words:
            words_dict[word]=words_dict[word]+1 if word in words_dict else 1

        for i in range(word_length):
            left=right=i
            curr_dict={}
            while right+word_length<=s_length:
                word=s[right:right+word_length]
                right+=word_length
                if word in words_dict:
                    curr_dict[word]=curr_dict[word]+1 if word in curr_dict else 1
                    while curr_dict[word]>words_dict[word]:
                        curr_dict[s[left:left+word_length]]-=1
                        left+=word_length
                    if right-left==words_length:
                        result.append(left)
                else:
                    curr_dict.clear()
                    left=right
        return result


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))