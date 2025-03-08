import heapq

class PathFinder:
    def __init__(self, board):
        # stores the board object and its dimensiom
        self.board = board 
        self.n = board.n 
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]  # defines right, down, left, up movements 

        # we will use an admissible heuristic based on the maximum cell value
        # we flatten the board into a list, and get the maximum cell value 
        flatten_values = [val for row in board.grid for val in row]
        self.max_val = max(flatten_values)  # this will give us the largest cell value

        # Keep track, globally, of the best path and sum found so far
        self.best_path = []
        self.best_sum = float('-inf')

    # we will figure out the upper bound on how much more we could collect if every unvisted cell had the maximum board value
    def _heuristic(self, x, y, visited_count):
        total_cells = self.n * self.n
        unvisited = total_cells - visited_count
        
        return unvisited * self.max_val # we ensure we never overestimate the possible future sum. Multiply unvisted cells by the max cell value to get max upperbound estimate
    

    # this function runs the A*-like search to find the maximum-sum path from (0,0) to (n-1, n-1)
    def find_best_path(self):

        start_visited = frozenset([(0,0)])  # we begin at the start node and use the frozenset to ensure we can reuse this immutable key
        
        # create the priority queue 
        pq = []
        
        # calculate the initial heuristic from (0,0)
        init_h = self._heuristic(0, 0, len(start_visited))

        # we use the negative priority since heap picks the smallest number first, but since we actually want the biggest first we make it negative
        # a bigger value will be selected first in the min-heap
        init_priority = -(0 + init_h)  
        
        # push initial state into the priority queue
        heapq.heappush(pq, (init_priority, 0, 0, start_visited, 0, [(0,0)]))

        # Create a dict to store the best sum we've found so far for each unique state
        # if we come across a state with a lower sum, we skip it
        best_seen = {}
        best_seen[(0,0, start_visited)] = 0

        # we will process the states based on which are most promising
        while pq:
            # here we will pop the state largest value (this is effectively the CurrentSum + heuristic)
            priority, x, y, visited_frozen_set, current_sum, path = heapq.heappop(pq)

            # we check if we already found a better sum for this state
            if best_seen.get((x, y, visited_frozen_set), float('-inf')) > current_sum:
                # if we did find that, no need to continue expanding
                continue

            # If we've reached the goal node (n-1, n-1), check if we have a better total sum than anew_y other previous attempts
            if (x, y) == (self.n - 1, self.n - 1):
                if current_sum > self.best_sum:
                    self.best_sum = current_sum
                    self.best_path = path
                continue

            # otherwise, we expand neighbors and explore each valid move (up/down/left/right)
            for delta_x, delta_y in self.directions:
                new_x, new_y = x + delta_x, y + delta_y

                # this portion is to ensure that the next move is indeed inside the board
                if 0 <= new_x < self.n and 0 <= new_y < self.n:
                    # we will only proceed if we have yet to visit that node
                    if (new_x, new_y) not in visited_frozen_set:
                        # We can add (new_x,new_y) to the path, which includes the value at the new node
                        new_sum = current_sum + self.board.get_value(new_x, new_y)
                        
                        # we should also create a new visited set, which will contain the old nodes as well as the new one 
                        new_visited = set(visited_frozen_set)
                        new_visited.add((new_x, new_y))
                        new_visited_frozen_set = frozenset(new_visited)
                        
                        # we check if we have found a better total for this state
                        if best_seen.get((new_x, new_y, new_visited_frozen_set), float('-inf')) < new_sum:
                            best_seen[(new_x, new_y, new_visited_frozen_set)] = new_sum

                            # Compute a new heuristic
                            # this involves how many nodes have not be visited yet multiplied by the max cell value
                            h = self._heuristic(new_x, new_y, len(new_visited_frozen_set))
                            # similarly, we use negative so that the largest value can be expanded first
                            new_priority = -(new_sum + h)
                            # we extend the path by this newly found node
                            new_path = path + [(new_x, new_y)]
                            # finally push this new state into the priority queue 
                            heapq.heappush(pq, (new_priority, new_x, new_y, new_visited_frozen_set, new_sum, new_path))

        # now, after exploring all possible states, best_path and best_sum contain the max solution
        return self.best_path, self.best_sum

