'''
https://leetcode.com/problems/multiply-strings/
43. Multiply Strings
Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1,len2=len(num1),len(num2)
        result=0
        for i in range(len1):
            for j in range(len2):
                factor1=(ord(num1[i])-ord('0'))*10**(len1-i-1)
                factor2=(ord(num2[j])-ord('0'))*10**(len2-j-1)
                result+=factor1*factor2
        result=''.join(str(result))
        return result


class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1,num2=num1[::-1],num2[::-1]
        len1,len2=len(num1),len(num2)
        temp=[0 for _ in range(len1+len2)]
        # Multiply
        for i in range(len1):
            for j in range(len2):
                temp[i+j]+=int(num1[i])*int(num2[j])
        carry=0
        digits=[]
        # Plus
        for num in temp:
            s=carry+num
            carry=s//10
            digits.append(str(s%10))
        result=''.join(digits)[::-1]
        # Remove zeros
        index=0
        for i in range(len1+len2-1):
            if result[i]=='0':
                index+=1
            else:
                break
        result=result[index:]
        return result


print(Solution().multiply('2','3'))
print(Solution().multiply('123','456'))