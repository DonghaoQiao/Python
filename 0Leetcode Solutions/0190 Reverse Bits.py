'''
https://leetcode.com/problems/reverse-bits/
190. Reverse Bits
Easy

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
so return 3221225471 which its binary representation is 10101111110010110010011101101001.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
will be given as signed integer type and should not affect your implementation, as the internal binary representation
of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above
the input represents the signed integer -3 and the output represents the signed integer -1073741825.
'''

class Solution():
    def reverseBits(self, n):
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

class Solution1():
    def reverseBits(self, n):
        x = 0
        for _ in range(32):
            x = x << 1
            if n & 1:
                x |= 1
            n = n >> 1
        return x

class Solution2():
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

print(Solution1().reverseBits(0b00000010100101000001111010011100))