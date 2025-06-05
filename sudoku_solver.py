class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9

    def is_valid(self, row, col, num):
        # Check row
        for x in range(self.size):
            if self.board[row][x] == num:
                return False

        # Check column
        for x in range(self.size):
            if self.board[x][col] == num:
                return False

        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def get_solution(self):
        if self.solve():
            return self.board
        return None 