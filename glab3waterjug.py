from collections import deque
def goal(state, target):
    return target in state
def successors(state, capacities):
    successors = []
    jug1, jug2 = state
    jug1_capacity, jug2_capacity = capacities
    successors.append((jug1_capacity, jug2))
    successors.append((jug1, jug2_capacity))
    successors.append((0, jug2))
    successors.append((jug1, 0))
    transfer = min(jug1, jug2_capacity - jug2)
    successors.append((jug1 - transfer, jug2 + transfer))
    transfer = min(jug2, jug1_capacity - jug1)
    successors.append((jug1 + transfer, jug2 - transfer))
    return successors
def dfs(capacities,target):
    stack=[(0,0)]
    visited=set()
    parent={}
    while stack:
        state=stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if goal(state,target):
            path=[]
            while state:
                path.append(state)
                state=parent.get(state)
            return path[::-1]
        for successor in successors(state,capacities):
            if successor not in visited:
                stack.append(successor)
                parent[successor]=state
    return None
jug1_capacity = 4
jug2_capacity = 3
target = 2
solution = dfs((jug1_capacity, jug2_capacity), target)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

           

