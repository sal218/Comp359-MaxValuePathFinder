import sys
import os

# this includes the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



from board import Board
from pathfinder import PathFinder

def main():
    print(" \nBoard size is 6 x 6: ")
    n = 6 
    
    grid = [
    [0, 1, 7, 1, 3, -2],
    [6, 5, 3, 10, 9, 8],
    [-3, -1, 1, -1, -4, 4],
    [-3, 10, 7, 4, 8, 6],
    [3, -4, 7, -1 , -1, 7],
    [8, 5, -5, -3 , -2, 0 ],
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
