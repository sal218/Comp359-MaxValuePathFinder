import sys
import os

# Allow importing from the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import tkinter as tk

from board import Board
from pathfinder import PathFinder

CELL_SIZE = 70  

def draw_board_and_path(canvas, board, path):
    n = board.n
    path_set = set(path)

    for i in range(n):
        for j in range(n):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            value = board.get_value(i, j)
            fill_color = "yellow" if (i, j) in path_set else "white"

            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")
            canvas.create_text(
                (x1 + x2) // 2,
                (y1 + y2) // 2,
                text=str(value),
                font=("Arial", 14, "bold")
            )

    for idx in range(len(path) - 1):
        (x_curr, y_curr) = path[idx]
        (x_next, y_next) = path[idx + 1]

        cx1 = y_curr * CELL_SIZE + (CELL_SIZE // 2)
        cy1 = x_curr * CELL_SIZE + (CELL_SIZE // 2)
        cx2 = y_next * CELL_SIZE + (CELL_SIZE // 2)
        cy2 = x_next * CELL_SIZE + (CELL_SIZE // 2)

        canvas.create_line(
            cx1, cy1, cx2, cy2,
            arrow=tk.LAST,
            width=2,
            fill="red",
            dash=(4, 2) 
        )

def run_gui(board, best_path, best_value):
    root = tk.Tk()
    root.title("6×6 Board Test")

    canvas_width = board.n * CELL_SIZE
    canvas_height = board.n * CELL_SIZE
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="gray90")
    canvas.pack(padx=10, pady=10)

    draw_board_and_path(canvas, board, best_path)

    info_label = tk.Label(root, text=f"Maximum Value Collected: {best_value}", font=("Arial", 12, "bold"))
    info_label.pack(pady=5)

    root.mainloop()

def main():
    print(" \nBoard size is 6 x 6: ")
    n = 6

    grid = [
        [  0,  -10, -10,  -10, -10, -10 ],
        [  3,   -9, -10,  -10, -10, -10 ],
        [ 10,  -1,   9,  -10, -10, -10 ],
        [ 8, 6,  5,   7, -10, -10 ],
        [ -10, -10, -4,   -1,  3,   2 ],
        [ -10, -10, -10,  -10,   1,   0 ],
    ]

    board = Board(n, grid=grid)
    print("\nBoard:")
    board.print_board()

    pathfinder = PathFinder(board)
    best_path, best_value = pathfinder.find_best_path()

    print("\n-------------------------------------")
    print("\nManually Determined Results:")
    print("\n-------------------------------------")

    print("\nThe Best Path is: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5)]")
    print("\nMaximum Value Collected: 43")

    print("\n-------------------------------------")
    print("\nAutogenrated Results Using Program:")
    print("\n-------------------------------------")
    print("\nThe Best Path is:", best_path)
    print(f"\nMaximum Value Collected: {best_value}\n")

    run_gui(board, best_path, best_value)

if __name__ == "__main__":
    main()
