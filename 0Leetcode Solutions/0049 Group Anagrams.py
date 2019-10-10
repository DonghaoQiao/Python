'''
https://leetcode.com/problems/group-anagrams/
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_map,result={},[]
        for s in strs:
            temp=''.join(sorted(s))
            if temp in strs_map:
                strs_map[temp].append(s)
            else:
                strs_map[temp]=[s]
        for s in strs_map.values():
            result.append(s)
        return result

strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))