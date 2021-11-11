import tkinter as tk
from SudokuSolver import SudokuSolver
import colors as c
import collectpuzzle


class Sudoku(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("9x9 Sudoku Solver")

        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=1000, height=1000
        )
        self.main_grid.grid(pady=(260, 10), padx=(10, 10))
        self.make_GUI()

        self.mainloop()

    def make_GUI(self):
        # make grid
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=50,
                    heigh=50
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                # setup cell validation
                entryText = tk.StringVar()
                vcmd = (self.register(self.onValidate), '%P', '%S')
                cell_value = tk.Entry(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    fg=c.CELL_NUMBER_COLOR,
                    font=c.CELL_FONT,
                    width=2,
                    textvariable=entryText,
                    validate="key",
                    validatecommand=vcmd
                )
                # initialize cells to '.' represents empty value
                cell_value.insert(0, '.')
                cell_value.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "value": cell_value}
                row.append(cell_data)
            self.cells.append(row)

        # make description header
        description_txt = """How do I use the solver?
        \nTo use the solver, simply enter numbers in the appropriate cells and click on the solve button.
        \nTo generate a random puzzle, click the randomize button.
        \n\n IMPORTANT NOTE: Cells are predefined with the value '.' which represents an empty cell. 
        To avoid errors, make sure empty cells have periods (.) in them."""
        description_frame = tk.Frame(self)
        tk.Label(
            description_frame,
            text=description_txt,
            font=c.DESCRIPTION_FONT,
            justify="center",
            wraplength=500
        ).grid(row=1)
        description_frame.place(relx=0.5, y=100, anchor="center")

        # make solve button
        solveButton = tk.Button(
            self,
            bg=c.SOLVE_BUTTON_COLOR,
            font=c.BUTTON_FONT,
            text="Solve",
            command=self.solvePuzzle,
            justify="center",
            height=2,
            width=8
        )
        solveButton.place(x=200, y=200)

        # make random puzzle button
        random_puzzle_button = tk.Button(
            self,
            bg=c.RANDOM_BUTTON_COLOR,
            font=c.BUTTON_FONT,
            text="Randomize",
            command=self.insertRandomPuzzle,
            justify="center",
            height=2,
            width=8
        )
        random_puzzle_button.place(x=300, y=200)

    def onValidate(self, P, S):
        # Disallow anything but numbers and '.' which represents empty cells
        if len(P) == 0:
            return True
        elif len(P) == 1 and ((S.isdigit() and 1 <= int(S) and int(S) <= 9) or S == "."):
            # Entry with 1 digit or . is ok
            return True
        else:
            # Anything else, reject it
            self.bell()
            return False

    def solvePuzzle(self):
        # extract the board from the entries
        unsolved_board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j]['value'].get()
                row.append(val)
            unsolved_board.append(row)

        # create a new SudokuSolver object with the unsolved_board and solve the puzzle
        solved_puzzle = SudokuSolver(board=unsolved_board)
        solved_puzzle.solveSudoku()
        self.insertPuzzle(solved_puzzle.board)

    def insertRandomPuzzle(self):
        # web scrape a random puzzle and then insert it into the window
        board = collectpuzzle.generateSudokuBoard()
        self.insertPuzzle(board)

    def insertPuzzle(self, board):
        # replace the unsolved version with solved version in the window
        for i in range(9):
            for j in range(9):
                self.cells[i][j]['value'].delete(0)
                self.cells[i][j]['value'].insert(0, board[i][j])


if __name__ == "__main__":
    Sudoku()
