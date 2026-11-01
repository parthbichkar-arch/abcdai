from collections import deque

grid = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0]
]

start = (0, 0)
goal = (6, 0)


def bfs(grid, start, goal):

    queue = deque([(start, [start])])
    visited = {start}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:

        current, path = queue.popleft()

        if current == goal:
            return path

        for dr, dc in directions:

            row = current[0] + dr
            col = current[1] + dc

            if (0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == 0 and
                (row, col) not in visited):

                visited.add((row, col))
                queue.append(((row, col), path + [(row, col)]))

    return None


solution_path = bfs(grid, start, goal)

if solution_path:
    print("!! Reached the Goal !!")
    print("Solution found!")
    print("Complete Path:")

    for step, position in enumerate(solution_path):
        print("Step", step, ":", position)

else:
    print("No solution found")