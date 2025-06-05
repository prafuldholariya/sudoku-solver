# Sudoku Solver

A Python application that solves Sudoku puzzles using a backtracking algorithm. The application features a graphical user interface where users can input their Sudoku puzzle and get the solution.

## Features

- Interactive 9x9 grid for puzzle input
- Input validation (only numbers 1-9 allowed)
- Clear grid functionality
- Instant solution generation
- Visual separation of 3x3 boxes

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- Pillow (for future image processing features)

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Enter your Sudoku puzzle by typing numbers 1-9 in the grid cells
3. Click "Solve" to get the solution
4. Click "Clear" to reset the grid

## How to Play

1. Enter the known numbers from your Sudoku puzzle into the grid
2. Leave empty cells blank (they will be filled with the solution)
3. Click "Solve" to see the solution
4. If the puzzle is invalid or has no solution, you'll see an error message

## Future Improvements

- Add image recognition for puzzle input
- Add puzzle generation feature
- Add difficulty levels
- Add save/load functionality 