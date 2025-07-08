class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def split_protein_chain(protein, k):
    # 1) count total nodes
    n = 0
    cur = protein
    while cur:
        n += 1
        cur = cur.next

    # 2) compute base size and remainder
    base, rem = divmod(n, k)

    parts = []
    cur = protein

    # 3) carve into k segments
    for i in range(k):
        part_head = cur
        # first rem parts get an extra node
        size = base + (1 if i < rem else 0)

        # advance to the end of this segment
        for _ in range(size - 1):
            if cur:
                cur = cur.next

        # detach
        if cur:
            nxt = cur.next
            cur.next = None
            cur = nxt

        parts.append(part_head)  # may be None if size == 0

    return parts

# --- Example usage ---
protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)
