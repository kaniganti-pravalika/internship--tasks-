class SudokuSolver:

    def __init__(self, board):
        self.board = board
        
        # Sets to store existing numbers for fast lookup
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        # Fill sets with initial board values
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != 0:
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.boxes[(r//3)*3 + (c//3)].add(num)

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-"*21)

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")

                print(self.board[i][j], end=" ")
            print()

    def solve(self):
        for r in range(9):
            for c in range(9):

                if self.board[r][c] == 0:

                    box_index = (r//3)*3 + (c//3)

                    for num in range(1, 10):

                        if (num not in self.rows[r] and
                            num not in self.cols[c] and
                            num not in self.boxes[box_index]):

                            # place number
                            self.board[r][c] = num
                            self.rows[r].add(num)
                            self.cols[c].add(num)
                            self.boxes[box_index].add(num)

                            if self.solve():
                                return True

                            # backtrack
                            self.board[r][c] = 0
                            self.rows[r].remove(num)
                            self.cols[c].remove(num)
                            self.boxes[box_index].remove(num)

                    return False
        return True


# Predefined Sudoku puzzle
board = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,2,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

solver = SudokuSolver(board)

print("Original Sudoku:\n")
solver.print_board()

if solver.solve():
    print("\nSolved Sudoku:\n")
    solver.print_board()
else:
    print("No solution exists")