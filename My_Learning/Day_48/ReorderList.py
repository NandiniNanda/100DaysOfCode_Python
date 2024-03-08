class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return head

    # Step 1: Find the middle of the linked list
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the linked list
    prev = None
    curr = slow.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    slow.next = None
    
    # Step 3: Merge the first half and the reversed second half alternatively
    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    
    return head

# Helper function to print the linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Test the function
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original linked list:")
printLinkedList(head)
reorderList(head)
print("Reordered linked list:")
printLinkedList(head)
