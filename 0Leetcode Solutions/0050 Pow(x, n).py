'''
https://leetcode.com/problems/powx-n/
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag=1 if n>=0 else -1
        result=1
        n=abs(n)
        while n>0:
            if n%2==1:
                result*=x
            n//=2
            x*=x
        if flag>0:
            return result
        else:
            return 1/result

print(Solution().myPow(2,10))
print(Solution().myPow(2.1,3))
print(Solution().myPow(2,-2))
