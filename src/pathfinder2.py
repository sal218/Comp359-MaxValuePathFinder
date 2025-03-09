import heapq

class PathFinder:
    def __init__(self, board):
        self.board = board
        self.n = board.n
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # right, down, left, up

    def flatten_grid(self):
        # Flatten the grid into a list of tuples with (x, y, value)
        flattened = []
        for i in range(self.n):
            for j in range(self.n):
                flattened.append((i, j, self.board.get_value(i, j)))
        return flattened

    def build_path_tree(self, current_x, current_y, path, current_value, visited):
        # Base case: if we've reached the end (bottom-right corner), return the path
        if (current_x, current_y) == (self.n - 1, self.n - 1):
            path.append((current_x, current_y))
            return path, current_value

        # Add current position to the visited set to prevent revisiting
        visited.add((current_x, current_y))
        best_path = None
        best_value = float('-inf')

        # Explore all possible directions
        for dx, dy in self.directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < self.n and 0 <= ny < self.n and (nx, ny) not in visited:
                # Accumulate the new value
                new_value = current_value + self.board.get_value(nx, ny)
                # Explore this path further
                new_path, new_total_value = self.build_path_tree(nx, ny, path + [(current_x, current_y)], new_value, visited)

                # If this new path has a better total value, keep it
                if new_total_value > best_value:
                    best_path = new_path
                    best_value = new_total_value

        visited.remove((current_x, current_y))
        return best_path, best_value

    def find_best_path(self):
        # Flatten the grid
        flattened = self.flatten_grid()

        # Initialize the starting point
        start_x, start_y, start_value = 0, 0, 0
        visited = set()
        best_path, best_value = self.build_path_tree(start_x, start_y, [], start_value, visited)

        return best_path, best_value
