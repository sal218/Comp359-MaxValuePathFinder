import heapq
from board import Board

class PathFinder:
    # stores the board object and its dimensiom
    def __init__(self, board):
        self.board = board
        # gets size of board
        self.n = board.n
        self.directions = [(1,0), (0,1), (0,-1), (-1,0)] # defines right, down, left, up movements 

        # we create a sorted list containing all cell values in descending order
        # This will alow us to estimate teh best possible sum remaining in the unexplored cells
        all_values = []
        for i in range(self.n):
            for j in range(self.n):
                all_values.append(self.board.get_value(i, j))
        self.sorted_values = sorted(all_values, reverse=True)

        self.best_value = float('-inf')
        self.best_path = []

    # this function will calculate the max poissible future gain from unexplored cells
    def possible_gain(self, visited_count):
        # store n x n total cells
        total_cells = self.n * self.n
        # calculate the remaining unvisted cells 
        unvisited = total_cells - visited_count
        if unvisited <= 0:
            return 0
        # sum the top m highest values from our sorted list to get estimated future gain (this helps with pruning)
        return sum(self.sorted_values[:unvisited])

    # we now implement the Best-First Search with bounding using prioirty queue     
    def branch_and_bound(self):
        # we first initiliaze the search
        start_visited = frozenset({(0,0)})
        start_state = (0, 0, start_visited)
        start_sum = 0
        start_path = [(0,0)]

        # we compute the initial priority 
        init_unvisited = (self.n * self.n) - len(start_visited) # determine the number of unvisted nodes/cells remaining 
        init_future = sum(self.sorted_values[:init_unvisited])  # we now get the best possible sum from the remaining highest values in our sorted array
        init_priority = start_sum + init_future # calcualte the priority which is 0 + init_future value

        priority_queue = []
        # push the initial state into the priority queue 
        heapq.heappush(priority_queue, (-init_priority, start_sum, 0, 0, start_visited, start_path)) # the reason for negative priority is so we can get the max value first

        # best_seen[(x, y, visitedSet)] = best sum found so far
        best_seen = {}
        best_seen[(0,0,start_visited)] = 0

        # we now expand the nodes in priority order
        while priority_queue:
            negative_priority, current_sum, x, y, visited_frozen_set, path = heapq.heappop(priority_queue) # we pop the highest-priority node 

            # If we've got a path to (n-1,n-1), check if total sum is the best found so far
            if (x, y) == (self.n - 1, self.n - 1):
                if current_sum > self.best_value:
                    self.best_value = current_sum
                    self.best_path = path
                continue

            # Skip if current sum is worse t avoid revisiting worse paths
            if best_seen.get((x, y, visited_frozen_set), float('-inf')) > current_sum:
                continue

            # we loop over each direction to get the next node (new_x, new_y)
            for delta_x, delta_y in self.directions: # using only the legal direction moves previous established to update x and y to new_x and new_y
                new_x, new_y = x + delta_x, y + delta_y # compute the next position
                # we explore only valid moves within board
                if 0 <= new_x < self.n and 0 <= new_y < self.n:
                    # check if we already visited the position (prevents revisiting old cells)
                    if (new_x, new_y) not in visited_frozen_set:
                        new_sum = current_sum + self.board.get_value(new_x, new_y) # adds the value of the new cell to our total sum
                        new_visited = set(visited_frozen_set) # track the visited cells for this path
                        new_visited.add((new_x, new_y)) # updates visited nodes by adding (new_x, new_y)
                        new_frozen_set = frozenset(new_visited) # updates our frozen set to contain the new node/cell

                        # check if the current sum is better than previously found sum. Reason for this is if we already visited this position with a better sum
                        # we skip this path entirely
                        old_sum = best_seen.get((new_x, new_y, new_frozen_set), float('-inf'))
                        if new_sum <= old_sum:
                            continue
                        
                        # update the best seen dictionary. This saves the best sum found so far for (new_x, new_y, new_frozen_set)
                        best_seen[(new_x, new_y, new_frozen_set)] = new_sum

                        # compute the max possible gain we can attain in the future (this is the bounding step)
                        visited_count = len(new_frozen_set)
                        future = self.possible_gain(visited_count)
                        # skip the paths the are not better than the best path (pruning step)
                        if new_sum + future <= self.best_value - 10: # allow for some flexibility/buffer before pruning to avoid removing a potentially more promising path
                            continue
                        
                        # add (push) the new path to the priority queue 
                        new_path = path + [(new_x, new_y)]
                        new_priority = new_sum + future
                        heapq.heappush(priority_queue, (-new_priority, new_sum, new_x, new_y, new_frozen_set, new_path))

                       

    def find_best_path(self):
        self.branch_and_bound()
        return self.best_path, self.best_value


