'''
https://leetcode.com/problems/reverse-integer/
7. Reverse Integer
Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0: return -self.reverse(-x)
        result=0
        while x:
            result=result*10+x%10
            x=x//10
        return result if result <= 2**31-1 else 0

print(Solution().reverse(-123))
print(Solution().reverse(28))
print(Solution().reverse(250))
