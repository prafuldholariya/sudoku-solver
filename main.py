import tkinter as tk
from tkinter import messagebox

from sudoku_solver import SudokuSolver


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("500x600")

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        # Create the Sudoku grid
        self.cells = {}
        self.create_grid()

        # Create buttons
        self.create_buttons()

        # Initialize the board
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(
                    self.main_frame, width=2, font=('Arial', 18), justify='center'
                )
                cell.grid(row=i, column=j, padx=1, pady=1)

                # Add thicker borders for 3x3 boxes
                if i % 3 == 0 and i != 0:
                    cell.grid(pady=(10, 1))
                if j % 3 == 0 and j != 0:
                    cell.grid(padx=(10, 1))

                # Validate input to only allow numbers 1-9
                vcmd = (self.root.register(self.validate_input), '%P')
                cell.config(validate='key', validatecommand=vcmd)

                self.cells[(i, j)] = cell

    def validate_input(self, value):
        if value == "":
            return True
        if value.isdigit() and 1 <= int(value) <= 9:
            return True
        return False

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        solve_button = tk.Button(
            button_frame,
            text="Solve",
            command=self.solve_sudoku,
            font=('Arial', 12),
            width=10,
        )
        solve_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_grid,
            font=('Arial', 12),
            width=10,
        )
        clear_button.pack(side=tk.LEFT, padx=5)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[(i, j)].get()
                row.append(int(value) if value else 0)
            board.append(row)
        return board

    def solve_sudoku(self):
        # Get the current board state
        self.board = self.get_board()

        # Create solver instance
        solver = SudokuSolver(self.board)

        # Solve the puzzle
        solution = solver.get_solution()

        if solution:
            # Update the grid with the solution
            for i in range(9):
                for j in range(9):
                    self.cells[(i, j)].delete(0, tk.END)
                    self.cells[(i, j)].insert(0, str(solution[i][j]))
        else:
            messagebox.showerror("Error", "No solution exists for this puzzle!")

    def clear_grid(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
