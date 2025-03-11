import tkinter as tk
from tkinter import simpledialog
from board import Board
from pathfinder import PathFinder

CELL_SIZE = 70  # Pixel size of each cell (can be adjusted)

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

            
            if (i, j) in path_set:
                fill_color = "yellow"
            else:
                fill_color = "white"

            
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")

            
            canvas.create_text(
                (x1 + x2) // 2,
                (y1 + y2) // 2,
                text=str(value),
                font=("Arial", 14, "bold")
            )

    for idx in range(len(path) - 1):
        (x_curr, y_curr) = path[idx]
        (x_next, y_next) = path[idx+1]

        
        cx1 = y_curr * CELL_SIZE + (CELL_SIZE // 2)
        cy1 = x_curr * CELL_SIZE + (CELL_SIZE // 2)

        
        cx2 = y_next * CELL_SIZE + (CELL_SIZE // 2)
        cy2 = x_next * CELL_SIZE + (CELL_SIZE // 2)

        
        canvas.create_line(cx1, cy1, cx2, cy2, arrow=tk.LAST, width=2, fill="red")


def main():
    
    root = tk.Tk()
    root.withdraw()  

    
    n_str = simpledialog.askstring("Board Size", "Enter board size (n x n):")
    if not n_str:
        
        return
    n = int(n_str)

    
    root.deiconify()
    root.title("Chessboard Path Visualizer")

    
    board = Board(n)

    
    pathfinder = PathFinder(board)
    best_path, best_value = pathfinder.find_best_path()

    
    print("Board:")
    board.print_board()
    print("\nBest Path:", best_path)
    print("Maximum Value Collected:", best_value)

    
    canvas_width = CELL_SIZE * n
    canvas_height = CELL_SIZE * n
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="gray90")
    canvas.pack(padx=10, pady=10)

    
    draw_board_and_path(canvas, board, best_path)

    
    info_label = tk.Label(
        root,
        text=f"Maximum Value Collected: {best_value}",
        font=("Arial", 12, "bold")
    )
    info_label.pack(pady=5)

    
    root.mainloop()

if __name__ == "__main__":
    main()
