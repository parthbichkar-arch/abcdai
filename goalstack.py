initial=['A','B','C']

goal=[('ON','A','B'),('ON','B','C')]


state=initial.copy()

stack=goal.copy()

while stack:
    action=stack.pop()

    if action[0]=='ON':

        a=action[1]
        b=action[2]

        if a in state and b in state:

            state.remove(a)
            state.remove(b)

            print("Move",a,"on",b)

            state.append(a+b)

print("final state:",state)

