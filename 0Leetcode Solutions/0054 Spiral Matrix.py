'''
https://leetcode.com/problems/spiral-matrix/
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        result=[]
        m,n=len(matrix),len(matrix[0])
        left,right,top,bottom=0,n-1,0,m-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            for i in range(top+1,bottom):
                result.append(matrix[i][right])
            for i in reversed(range(left,right+1)):
                if top<bottom:
                    result.append(matrix[bottom][i])
            for i in reversed(range(top+1,bottom)):
                if left<right:
                    result.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        return result

print(Solution().spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]]))