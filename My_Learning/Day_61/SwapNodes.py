class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first_node = prev.next
        second_node = prev.next.next

        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev = first_node

    return dummy.next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head)

new_head = swapPairs(head)

print("\nLinked list after swapping pairs:")
printLinkedList(new_head)
