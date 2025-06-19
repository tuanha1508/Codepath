from collections import deque
def blueprint_approval(blueprints):
    pass
    q = deque(blueprints)
    approved = []

    while q:
        current_min = min(q)

        while q[0] != current_min:
            q.append(q.popleft())

        approved.append(q.popleft())

    return approved

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 