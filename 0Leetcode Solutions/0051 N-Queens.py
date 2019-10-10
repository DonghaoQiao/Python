'''
https://leetcode.com/problems/n-queens/
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(r,c):
            for i in range(r):
                if board[i]==c or abs(r-i)==abs(board[i]-c):
                    return False
            return True
        def dfs(row,valuelist):
            if row==n:
                result.append(valuelist)
                return
            for i in range(n):
                if check(row,i):
                    board[row]=i
                    s='.'*n
                    dfs(row+1,valuelist+[s[:i]+'Q'+s[i+1:]])
        board=[-1 for _ in range(n)]
        result=[]
        dfs(0,[])
        return result


class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def recursive(row,column):
            if row==n:
                result.append(list(map(lambda x:'.'*x+'Q'+'.'*(n-1-x),column)))
            else:
                for i in range(n):
                    if not col[i] and not diag[row+i] and not anti_diag[n-i+row]:
                        col[i]=diag[row+i]=anti_diag[n-i+row]=True
                        recursive(row+1,column+[i])
                        col[i]=diag[row+i]=anti_diag[n-i+row]=False
        col=[False]*n
        diag=[False]*(2*n)
        anti_diag=[False]*(2*n)
        result=[]
        recursive(0,[])
        return result


print(Solution().solveNQueens(4))