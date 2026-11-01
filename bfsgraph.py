from collections import deque

grid=[
    [0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0],
    [0,0,0,0,1,0,0],
    [0,0,1,0,1,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0]

]

start=(0,0)
goal=(6,0)

def bfs(grid,start,goal):

    queue=deque([start],)