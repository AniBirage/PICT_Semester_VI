import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Heuristic cost from this node to goal node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic_cost_estimate(current, goal):
    return abs(current.position[0] - goal.position[0]) + abs(current.position[1] - goal.position[1])

def reconstruct_path(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def a_star(grid, start, goal):
    open_list = []
    closed_set = set()
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal_node.position:
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.position)
        
        for next_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Four directions: up, down, left, right
            new_position = (current_node.position[0] + next_position[0], current_node.position[1] + next_position[1])
            
            if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]):
                continue
            
            if grid[new_position[0]][new_position[1]] == 1:
                continue
            
            if new_position in closed_set:
                continue
            
            new_node = Node(new_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = heuristic_cost_estimate(new_node, goal_node)
            new_node.f = new_node.g + new_node.h
            
            heapq.heappush(open_list, new_node)
    
    return None  # No path found

def input_grid():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    grid = []
    print("Enter the grid (0 for empty space, 1 for obstacle):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Invalid input. Number of columns doesn't match.")
            return None
        grid.append(row)
    return grid

def input_position(message):
    while True:
        try:
            x, y = map(int, input(message).split())
            return x, y
        except ValueError:
            print("Invalid input. Please enter two integers separated by space.")

if __name__ == "__main__":
    grid = input_grid()
    if grid:
        start = input_position("Enter start position (row column): ")
        goal = input_position("Enter goal position (row column): ")
        path = a_star(grid, start, goal)
        if path:
            print("Path found:", path)
        else:
            print("No path found")
