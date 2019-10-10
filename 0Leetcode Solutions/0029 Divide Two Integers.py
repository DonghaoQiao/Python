'''
https://leetcode.com/problems/divide-two-integers/
29. Divide Two Integers
Medium

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function
returns 231 − 1 when the division result overflows.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MIN_INT,MAX_INT=-2**31,2**31-1
        result=0
        sign=(dividend<0)is(divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)

        while dividend>=divisor:
            temp,i=divisor,1
            while dividend>=temp:
                dividend-=temp
                result+=i
                i<<=1
                temp<<=1
        if not sign:
            result=-result
        return max(min(result,MAX_INT),MIN_INT)


print(Solution().divide(10,3))
print(Solution().divide(7,-3))
print(Solution().divide(-2**31,-1))