class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand: Node, m: int, n: int) -> Node:
    current = dna_strand
    while current:
        for i in range(1, m):
            if current.next:
                current = current.next
            else:
                return dna_strand
        to_delete = current.next
        for i in range(n):
            if to_delete:
                to_delete = to_delete.next
            else:
                break
        current.next = to_delete
        current = to_delete
    return dna_strand

# Example Usage
vals = list(range(1, 14))
head = Node(vals[0])
cur = head
for v in vals[1:]:
    cur.next = Node(v)
    cur = cur.next

edited = edit_dna_sequence(head, m=2, n=3)
print_linked_list(edited)
