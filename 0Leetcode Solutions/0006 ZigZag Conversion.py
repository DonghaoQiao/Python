'''
https://leetcode.com/problems/zigzag-conversion/
6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l=len(s)
        matrix=[[] for _ in range(numRows)]
        i=0
        while i<l:
            try:
                for j in range(numRows):
                    matrix[j].append(s[i])
                    i+=1
                for j in range(numRows-2,0,-1):
                    matrix[j].append(s[i])
                    i += 1
            except IndexError:
                break

        lst=[''.join(element) for element in matrix]
        return ''.join(lst)

class Solution1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        step,zigzag=2*numRows-2,''
        for i in range(numRows):
            for j in range(i,len(s),step):
                zigzag+=s[j]
                if 0<i<numRows-1 and j+step-2*i<len(s):
                    zigzag+=s[j+step-2*i]
        return zigzag


print(Solution1().convert("abcdef",3))

print(Solution1().convert("PAYPALISHIRING",3))