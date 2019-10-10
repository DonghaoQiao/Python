'''
https://leetcode.com/problems/n-queens-ii/
52. N-Queens II
Hard

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(r,c):
            for i in range(r):
                if board[i]==c or abs(r-i)==abs(board[i]-c):
                    return False
            return True
        def dfs(row):
            if row==n:
                return 1
            result=0
            for i in range(n):
                if check(row,i):
                    board[row]=i
                    result+=dfs(row+1)
            return result
        board=[-1 for _ in range(n)]
        return dfs(0)

print(Solution().totalNQueens(4))