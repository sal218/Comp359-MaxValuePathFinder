
class PathFinder:
    def __init__(self, board):
         # stores the board object and its dimensiom
        self.board = board
        self.n = board.n
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # defines right, down, left, up movements 

    def flatten_grid(self):
        # we flatten the board into a list of containing tuples x, y, and value
        flattened = []
        # we now loop over each row (i) abd each column (j) in the board
        for i in range(self.n):
            for j in range(self.n):
                # we appeach a tuple i, j, cell_value
                flattened.append((i, j, self.board.get_value(i, j)))
        # we return the list of all cells with their coordinates and values
        return flattened

    def build_path_tree(self, current_x, current_y, path, current_value, visited):
        # This is considered our base case. We check if we're alreadelta_y at the bottom-right corner (n-1, n-1)
        if (current_x, current_y) == (self.n - 1, self.n - 1):
            # if we are, then we append (current_x, current_y) to path
            path.append((current_x, current_y))
            # we return the path and the total value so far
            return path, current_value

        
        visited.add((current_x, current_y)) # we now mark our current node so we dont revist unnessarily 
        # we also keep track of the best path and best value
        best_path = None
        best_value = float('-inf')

        # we loop over each direction to get the next node (new_x, new_y)
        for delta_x, delta_y in self.directions:
            new_x, new_y = current_x + delta_x, current_y + delta_y

            # this portion is to ensure that the next move is indeed inside the board and not already visited
            if 0 <= new_x < self.n and 0 <= new_y < self.n and (new_x, new_y) not in visited:
                # we udpate the values and store in new_x and new_y which account for total value so far plus the value of the new cell
                new_value = current_value + self.board.get_value(new_x, new_y)
                # we now recursively call build_path_tree to continue exploring deeper from (new_x, new_y).
                # we pass an updated path plus the current_x and current_y and the new sum
                new_path, new_total_value = self.build_path_tree(new_x, new_y, path + [(current_x, current_y)], new_value, visited)

                # If new_path and new_total_value is bigger than our best_value, we update best_path and best_value
                if new_total_value > best_value:
                    best_path = new_path
                    best_value = new_total_value

        # backtracking: after exploring all directions, we then remove (current_x, current_y) from visited so we can use it again in other branches of the search
        visited.remove((current_x, current_y))
        # return best path and best value from this call
        return best_path, best_value

    def find_best_path(self):
        flattened = self.flatten_grid()

        # set the starting point to 0,0 to with an initial value of 0
        start_x, start_y, start_value = 0, 0, 0
        visited = set()
        # call build_path_Tree with these starting parameters
        best_path, best_value = self.build_path_tree(start_x, start_y, [], start_value, visited)

        # returns final answer
        return best_path, best_value
