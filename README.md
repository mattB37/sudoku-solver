# sudoku-solver

How do I use this sudoku solver on my machine?
  - To use the program, install the package and install the required libraries from the requirements.txt file
  - Simply run the main.py file and this will open up the gui where you can input a puzzle, solve a puzzle, or generate a random unsolved puzzle

How does the Solver solve puzzles?
  - The solver visits every empty cell, filling in digits and backtracking whenever a number is found to be invalid
  - It can solve almost every puzzle in under 1 second

Random unsolved puzzles are scraped from https://menneske.no/sudoku/eng/ using the Python 3 webscraping library BeautifulSoup. 

