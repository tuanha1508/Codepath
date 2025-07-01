class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head is None:
        print("Aw! Better luck next time!")
        return None
    print(f"I caught a {head.fish_name}!")
    return head.next

if __name__ == "__main__":
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    empty_list = None

    print_linked_list(fish_list) 
    new_head = catch_fish(fish_list)
    print_linked_list(new_head)
    print(catch_fish(empty_list))
