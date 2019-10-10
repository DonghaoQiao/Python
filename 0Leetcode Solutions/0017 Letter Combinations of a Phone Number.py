'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        lookup=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result=['']
        for digit in reversed(digits):
            choices=lookup[int(digit)]
            m,n=len(choices),len(result)
            result+=[result[i%n] for i in range(n,m*n)]

            for i in range(m*n):
                result[i]=choices[i//n]+result[i]
        return result

class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        def dfs(num, string, result):
            if num==len(digits):
                result.append(string)
                return
            for letter in lookup[digits[num]]:
                dfs(num+1,string+letter,result)

        lookup={'1':[''],
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        result=[]
        dfs(0,'',result)
        return result
print(Solution().letterCombinations('23'))