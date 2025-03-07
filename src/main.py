
from board import Board
from pathfinder import PathFinder

def main():
    n = int(input("\nEnter board size (n x n): "))

    board = Board(n)
    print("\nGenerated Board:")
    board.print_board()

    pathfinder = PathFinder(board)
    best_path, best_value = pathfinder.find_best_path()

    print("\nThe Best Path is:", best_path)
    print(f"Maximum Value Collected: {best_value}\n")

if __name__ == "__main__":
    main()
