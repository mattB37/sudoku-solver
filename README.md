# sudoku-solver

This is a basic sudoku solver program that solves 9x9 sudoku boards. 

Random unsolved puzzles are pulled from https://menneske.no/sudoku/eng/ using the Python 3 webscraping library BeautifulSoup. 
The solver uses a brute force depth-first-search that visits every empty cell, filling in digits and backtracking whenever a number is found to be invalid.
