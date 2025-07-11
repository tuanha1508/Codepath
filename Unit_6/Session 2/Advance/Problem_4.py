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

def playlist_overlap(playlist_a, playlist_b):
    pa, pb = playlist_a, playlist_b
    while pa is not pb:
        pa = pa.next if pa else playlist_b
        pb = pb.next if pb else playlist_a
    
    return pa
playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

print((playlist_overlap(playlist_a, playlist_b)).value)