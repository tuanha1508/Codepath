class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def max_protein_pair_stability(head: Node) -> int:
    vals = []
    curr = head
    while curr:
        vals.append(curr.value)
        curr = curr.next
    n = len(vals)
    max_sum = 0
    for i in range(n // 2):
        s = vals[i] + vals[n - 1 - i]
        if s > max_sum:
            max_sum = s
    return max_sum

head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))
