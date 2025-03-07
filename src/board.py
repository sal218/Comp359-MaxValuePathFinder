# could use this for board creation and value assignments
import random

class Board:
    # constructor to initialize a board of size nxn
    def __init__(self, n, grid = None ,min_value=-5, max_value=10):
        self.n = n
        if grid:
            self.grid = grid
        else:
            self.grid = self._generate_board(min_value, max_value) # calls the generate method to generate a random grid and stores in self.grid

    # creates a 2D list where each cell will have a random value between min_value and max_value
    def _generate_board(self, min_value, max_value):
        # this should generate values for every position on the chess board except start and stop positions
        board = [[random.randint(min_value, max_value) for _ in range(self.n)] for _ in range(self.n)]
        board[0][0] = 0 # we set start position to have no value
        board[self.n - 1][self.n - 1] = 0 # this will define the end or goal node which should also have no value
        return board

    # this function will print out the board in a readable format
    def print_board(self):
        for row in self.grid:
            print("  ".join(f"{val: 2}" for val in row))

    # this will return the value at (x,y) in the grid which will be used to define the final path
    def get_value(self, x, y):
        return self.grid[x][y]
