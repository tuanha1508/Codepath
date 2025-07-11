class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> " if curr.next else "")
        curr = curr.next
    print()

def merge_playlists(playlist1, playlist2, a, b):
    dummy = Node(None, playlist1)
    prev_a = dummy
    for _ in range(a):
        prev_a = prev_a.next
    post_b = prev_a.next
    for _ in range(b - a + 1):
        post_b = post_b.next
    prev_a.next = playlist2
    tail2 = playlist2
    if tail2:
        while tail2.next:
            tail2 = tail2.next
        tail2.next = post_b
    else:
        prev_a.next = post_b
        
    return dummy.next
playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))