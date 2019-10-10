'''
https://leetcode.com/problems/integer-to-english-words/
273. Integer to English Words
Hard

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


class Solution():
    def numberToWords(self, num):
        l1='Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        l2='Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        l3='Hundred'
        l4='Thousand Million Billion'.split()
        result,digits=[],0
        while num:
            word=''
            sign,num=num%1000,num//1000
            if sign>99:
                word+=l1[sign//100]+' '+l3+' '
                sign%=100
            if sign>19:
                word+=l2[sign//10-2]+' '
                sign%=10
            if sign>0:
                word+=l1[sign]+' '
            word=word.strip()
            if word:
                word+=' '+l4[digits-1] if digits else ''
                result+=word,
            digits+=1
        return result or 'Zero'


print(Solution().numberToWords(123))
print(Solution().numberToWords(12345))
print(Solution().numberToWords(1234567))
print(Solution().numberToWords(1234567891))