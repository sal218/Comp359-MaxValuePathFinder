# used for writing the algorithm that solves the question
import heapq

class PathFinder():
    # constructor which stores board reference and its size, and defines legal movements
    def __init__(self, board):
        self.board = board
        self.n = board.n
        self.directions = [[0,1], [1,0], [0,-1], [-1,0]] # defines right, down, left, up movements 

    # we will use the heuristic to determine the maximum value remaining. It estimates the best possible gain from (x,y) to (n-1, n-1)
    def heuristic(self, x, y):
        max_value = max(max(row) for row in self.board.grid if row) # determines max cell value
        return (self.n -1 - x) + (self.n - 1 - y) * max_value # this is known as manhattan distance, which we then multiply by the max value
    
    # we then build the A* algorithm to utilize the heuristic to find the highest-value-path from (0,0) to (n-1, n-1)
    def find_best_path(self):
        priority_queue = []
        heapq.heappush(priority_queue, (-0,0,0,[(0,0)]))

        # initializes a visisted set and tracks the best path
        visited = set()
        best_value = float('-inf')
        best_path = []

        while priority_queue:
            # extracts the highest value path so far
            neg_g, x, y, path = heapq.heappop(priority_queue)
            g = -neg_g # used to convert back to positive value

            # ensures we do not visit a cell twice
            if (x,y) in visited:
                continue
            visited.add((x,y))
            
            # if we reach (n-1, n-1) then we update the best path
            if (x,y) == (self.n -1 , self.n -1):
                if g > best_value:
                    best_value = g
                    best_path = path
                continue
            
            # we expand the neighbors, calculate new value for the path and then push it into the heap
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.n and 0 <= ny < self.n and (nx,ny) not in visited:
                    new_value = g + self.board.get_value(nx,ny)
                    heapq.heappush(priority_queue, (-new_value, nx, ny, path + [(nx, ny)]))

        # finally return optimal path and total value of the path
        return best_path, best_value

