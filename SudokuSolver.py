class SudokuSolver:

    def __init__(self, board, empty_cell='.'):
        self.board = board
        self.empty_cell = empty_cell

    def solveSudoku(self):
        """
        Solves a sudoku puzzle using a backtracking algorithm
        """
        self.solve(row=0, col=0)

    def solve(self, row, col):
        """
        Recursively backtracks and performs a depth-first search to solve a sudoku board
        """
        # base cases
        if col == len(self.board[row]):  # reached the end of a row
            col = 0
            row += 1
            if row == len(self.board):  # solved the board
                return True
        # skip already filled in entries
        if self.board[row][col] != self.empty_cell:
            return self.solve(row, col+1)
        # try 1-9 in cell
        for numToPlace in map(str, range(1, 10)):
            if self.validLocation(row, col, numToPlace):
                self.board[row][col] = numToPlace
                if self.solve(row, col+1):
                    return True
                self.board[row][col] = self.empty_cell
        return False

    def validLocation(self, row, col, val):
        """
        Returns false if placing val at the current position invalidates the sudoku board
        """
        if self.checkRow(row, val) and self.checkCol(col, val) and self.checkBox(row, col, val):
            return True
        return False

    def checkRow(self, row, val):
        """
        Returns true if the current row is valid
        """
        for col in range(9):
            if self.board[row][col] == val:
                return False
        return True

    def checkCol(self, col, val):
        """
        Returns true if the current column is valid
        """
        for row in range(9):
            if self.board[row][col] == val:
                return False
        return True

    def checkBox(self, row, col, val):
        """
        Returns true if the 3x3 box at the current row and column is valid
        """
        rowBox, colBox = (row//3)*3, (col//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[rowBox+i][colBox+j] == val:
                    return False
        return True

    def __repr__(self):
        res = ""
        for row in range(9):
            res += str(self.board[row]) + "\n"
        return res
