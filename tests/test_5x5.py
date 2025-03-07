import sys
import os

# this includes the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



from board import Board
from pathfinder import PathFinder

def main():
    print(" \nBoard size is 5 x 5: ")
    n = 5 
    
    grid = [
    [0, 4, 3, 12, 2],
    [-6, -1, 2, 1, 4],
    [-4, 10, 6, -5, 4],
    [11, 13, -5, 5 , 10],
    [3, -2, 1, 4 , 0],
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
