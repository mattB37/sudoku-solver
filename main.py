from sudoku.solver.SudokuSolver import SudokuSolver as Solver
from sudoku.collectpuzzle import generateSudokuBoard
from timeit import default_timer as timer


def print_format(board: list):
    """Converts 2d array into readable string output"""
    return '[' + '\n['.join([', '.join(row) + ']' for row in board])


def main():
    """Creates an unsolved sudoku board, then outputs both the unsolved and solved boards"""
    sudoku_board = generateSudokuBoard()
    print("The unsolved sudoku board:\n" + print_format(sudoku_board))
    board = Solver(sudoku_board)
    start = timer()
    board.solveSudoku()
    end = timer()
    elapsed_time = round(end-start, 4)
    print("\nThe solved sudoku board:")
    print(f"Time to solve: {elapsed_time}s")
    print(print_format(sudoku_board))


if __name__ == "__main__":
    main()
