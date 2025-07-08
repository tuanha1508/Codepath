class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return []
    slow = protein
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    start = slow
    result = []
    node = start
    while True:
        result.append(node.value)
        node = node.next
        if node is start:
            break
    return result

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next
print(cycle_length(protein_head))
