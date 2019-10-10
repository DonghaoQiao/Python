'''
https://leetcode.com/problems/palindrome-number/
9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y,z=0,x
        while x>0:
            y=y*10+x%10
            x//=10
        return y==z


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(1221))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))