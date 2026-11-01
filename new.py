def dfs(a, b, visited):

    if (a, b) in visited:
        return False

    visited.add((a, b))
    print(a, b)

    # Goal: 2 litres in first jug
    if a == 2:
        print("Goal Reached!")
        return True

    # Possible operations
    states = [
        (4, b),  # Fill 4L jug
        (a, 3),  # Fill 3L jug
        (0, b),  # Empty 4L jug
        (a, 0),  # Empty 3L jug

        # Pour 4L jug into 3L jug
        (a - min(a, 3-b), b + min(a, 3-b)),

        # Pour 3L jug into 4L jug
        (a + min(b, 4-a), b - min(b, 4-a))
    ]

    for state in states:
        if dfs(state[0], state[1], visited):
            return True

    return False


visited = set()

dfs(0, 0, visited)