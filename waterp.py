def get_next_state(a,b):
    A,B=4,3

    #fill either jug
    states=[(A,b),(a,B)]

    #empty either jug
    states+=[(0,b),(a,0)]

    #pour 3L into 4L
    pour=min(b,A-a)
    states.append((a + pour,b - pour))

    #pour 4L into 3L
    pour=min(a,B-b)
    states.append((a - pour,b + pour))


    return states

def dfs(state,visited):
    a,b=state
    if a==2 or b==2:
        return[state]

    visited.add(state)

    for next_states in get_next_state(a,b):
        if next_states  not in visited:
            result =dfs(next_states,visited)

            if result:
                return[state]+result

    return None

path=dfs((0,0),set())

if path:
    for state in path:
        print(state)
    print("Goal is reached!")
else:
    print("No solution found!")

    
