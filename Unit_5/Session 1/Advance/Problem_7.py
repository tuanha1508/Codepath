class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    total = 0
    count = 0
    current = head
    while current:
        total += 1
        if current.fish_name == fish_name:
            count += 1
        current = current.next
    if total == 0:
        return 0.00
    probability = count / total
    return int(probability * 100) / 100

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))
