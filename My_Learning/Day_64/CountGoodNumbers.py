class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodesWithGreaterValues(head):
    if not head:
        return None
    
    # Dummy node to handle cases where the head itself needs to be removed
    dummy = ListNode(0)
    dummy.next = head
    
    max_val = float('-inf')
    current = head
    prev = dummy
    
    while current:
        if current.val < max_val:
            # Remove the current node
            prev.next = current.next
        else:
            # Update the maximum value encountered so far
            max_val = max(max_val, current.val)
            prev = current
        current = current.next
    
    return dummy.next

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked list: 5 -> 2 -> 13 -> 3 -> 8
head1 = ListNode(5)
head1.next = ListNode(2)
head1.next.next = ListNode(13)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(8)

print("Original linked list:")
printLinkedList(head1)

# Remove nodes with greater values
new_head1 = removeNodesWithGreaterValues(head1)

print("\nModified linked list:")
printLinkedList(new_head1)


# Create the linked list: 1 -> 1 -> 1 -> 1
head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(1)

print("\nOriginal linked list:")
printLinkedList(head2)

# Remove nodes with greater values
new_head2 = removeNodesWithGreaterValues(head2)

print("\nModified linked list:")
printLinkedList(new_head2)
