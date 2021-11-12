from bs4 import BeautifulSoup
import requests
import time


def scrapePuzzle():
    """Returns a list of strings that represent an unsolved 9x9 sudoku puzzle"""
    page = requests.get("https://menneske.no/sudoku/eng/").text
    soup = BeautifulSoup(page, "lxml")
    puzzle = []
    rows = soup.find_all("tr", {"class": "grid"})
    for row in rows:
        cols = row.find_all("td")
        for col in cols:
            txt = col.text
            if txt != "\xa0":
                puzzle.append(txt)
            else:
                puzzle.append(".")
    return puzzle


def formatSudokuPuzzle(puzzle: str):
    """Converts an 81 character string that represents a sudoku board into a 2d array"""
    sudokuBoard = []
    n = 9
    for i in range(0, len(puzzle), n):
        sudokuBoard.append(list(puzzle[i : i + n]))
    return sudokuBoard


def generateSudokuBoard():
    """Returns a 2d array representation of an unsolved 9x9 sudoku board"""
    return formatSudokuPuzzle(scrapePuzzle())


def main():
    """Scrapes a new board from the website"""
    board = generateSudokuBoard()
    print(board)
    for row in board:
        print(row)


if __name__ == "__main__":
    main()
