'''
https://leetcode.com/problems/sudoku-solver/
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y]==board[x][y]:
                    return False
            for j in range(9):
                if j != y and board[x][j]==board[x][y]:
                    return False
            for i in range(3):
                i+=x//3*3
                for j in range(3):
                    j+=y//3*3
                    if (i != x or j != y) and board[i][j]==board[x][y]:
                        return False
            return True
        def solver(board):
            point='.'
            for i in range(9):
                for j in range(9):
                    if board[i][j]==point:
                        for k in range(9):
                            board[i][j]=chr(ord('1')+k)
                            if isValid(board,i,j) and solver(board):
                                return True
                            board[i][j]=point
                        return False
            return True
        solver(board)

# 一段很长但是运行很快的代码
class Solution1(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
    col_size = 9  # len(self.board)
    row_size = 9  # len(self.board[0])
    block_col_size = 3
    block_row_size = 3
    digits = '123456789'
    empty_symbol = '.'

    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        self.init(board)
        self.solve()

    def init(self, board):
        self.board = board

        # list all empty cells. a `cell` is a tuple `(row_index, col_index)`
        self.empty_cells = set([(ri, ci) for ri in range(self.row_size) for ci in range(self.col_size) if self.board[ri][ci] == self.empty_symbol])

        # find candidates of each cell
        self.candidates = [[set(self.digits) for ci in range(self.col_size)] for ri in range(self.row_size)]
        for ri in range(self.row_size):
            for ci in range(self.col_size):
                digit = self.board[ri][ci]
                if digit != self.empty_symbol:
                    self.candidates[ri][ci] = set()
                    self.update_candidates((ri, ci), digit)

    def solve(self):
        # if there are no empty cells, it's solved
        if not self.empty_cells:
            return True

        # get the cell with fewest candidates
        cell = min(self.empty_cells, key=lambda cell: len(self.candidates[cell[0]][cell[1]]))

        # try filling the cell with one of the candidates, and solve recursively
        ri, ci = cell
        for digit in list(self.candidates[ri][ci]):
            candidate_updated_cells = self.fill_cell(cell, digit)
            solved = self.solve()
            if solved:
                return True
            self.unfill_cell(cell, digit, candidate_updated_cells)

        # if no solution found, go back and try the next candidates
        return False

    def fill_cell(self, cell, digit):
        # fill the cell with the digit
        ri, ci = cell
        self.board[ri][ci] = digit

        # remove the cell from empty_cells
        self.empty_cells.remove(cell)

        # update the candidates of other cells
        # keep a list of updated cells. will be used when unfilling cells
        candidate_updated_cells = self.update_candidates(cell, digit)

        return candidate_updated_cells

    def unfill_cell(self, cell, digit, candidate_updated_cells):
        # unfill cell
        ri, ci = cell
        self.board[ri][ci] = self.empty_symbol

        # add the cell back to empty_cells
        self.empty_cells.add(cell)

        # add back candidates of other cells
        for ri, ci in candidate_updated_cells:
            self.candidates[ri][ci].add(digit)

    def update_candidates(self, filled_cell, digit):
        candidate_updated_cells = []
        for ri, ci in self.related_cells(filled_cell):
            if (self.board[ri][ci] == self.empty_symbol) and (digit in self.candidates[ri][ci]):
                self.candidates[ri][ci].remove(digit)
                candidate_updated_cells.append((ri, ci))
        return candidate_updated_cells

    def related_cells(self, cell):
        return list(set(self.cells_in_same_row(cell) + self.cells_in_same_col(cell) + self.cells_in_same_block(cell)))

    def cells_in_same_row(self, cell):
        return [(cell[0], ci) for ci in range(self.col_size)]

    def cells_in_same_col(self, cell):
        return [(ri, cell[1]) for ri in range(self.row_size)]

    def cells_in_same_block(self, cell):
        block_first_cell_ri = (cell[0] // self.block_row_size) * self.block_row_size
        block_first_cell_ci = (cell[1] // self.block_col_size) * self.block_col_size
        return [
            (block_first_cell_ri + in_block_ri, block_first_cell_ci + in_block_ci)
            for in_block_ri in range(self.block_row_size)
            for in_block_ci in range(self.block_col_size)
        ]

board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sudoku=[
  ["5","3","4","6","7","8","9","1","2"],
  ["6","7","2","1","9","5","3","4","8"],
  ["1","9","8","3","4","2","5","6","7"],
  ["8","5","9","7","6","1","4","2","3"],
  ["4","2","6","8","5","3","7","9","1"],
  ["7","1","3","9","2","4","8","5","6"],
  ["9","6","1","5","3","7","2","8","4"],
  ["2","8","7","4","1","9","6","3","5"],
  ["3","4","5","2","8","6","1","7","9"]
]

Solution().solveSudoku(board)
assert(board==sudoku)
