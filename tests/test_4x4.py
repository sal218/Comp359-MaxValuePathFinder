import sys
import os

# this includes the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



from board import Board
from pathfinder import PathFinder

def main():
    print(" \nBoard size is 4 x 4: ")
    n = 4 
    
    grid = [
    [0, -4, 3, 2],
    [1, 0, 3, 4],
    [-2, 1, 7, -5],
    [6, 2, 5, 0]
    ]

    board = Board(n, grid = grid)
    
    print("\n Board:")

    board.print_board()

    pathfinder = PathFinder(board)
    best_path, best_value = pathfinder.find_best_path()

    print("\nThe Best Path is:", best_path)
    print(f"Maximum Value Collected: {best_value}\n")

if __name__ == "__main__":
    main()
