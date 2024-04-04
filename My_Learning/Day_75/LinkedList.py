class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head: 'Node') -> 'Node':
    if not head:
        return None

    def flatten_util(curr):
        while curr:
            if curr.child:
                child_head = curr.child
                child_tail = flatten_util(child_head)
                child_tail.next = curr.next
                if curr.next:
                    curr.next.prev = child_tail
                curr.next = child_head
                child_head.prev = curr
                curr.child = None
                curr = child_tail
            if not curr.next:
                break
            curr = curr.next
        return curr

    flatten_util(head)
    return head

# Example usage:
# Construct the multilevel doubly linked list
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next
head.next.child = Node(7)
head.next.child.next = Node(8)
head.next.child.next.prev = head.next.child
head.next.child.next.next = Node(11)
head.next.child.next.next.prev = head.next.child.next
head.next.next.next.child = Node(9)
head.next.next.next.child.next = Node(10)
head.next.next.next.child.next.prev = head.next.next.next.child
head.next.next.next.child.child = Node(12)

# Flatten the multilevel doubly linked list
flattened_head = flatten(head)

# Print the flattened list
current = flattened_head
while current:
    print(current.val, end=" -> ")
    current = current.next
