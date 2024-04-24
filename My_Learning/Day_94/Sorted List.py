import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap to store (value, node) pairs
    min_heap = []
    
    # Add the head of each linked list to the min-heap
    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.val, head))
    
    # Create a dummy node to build the merged list
    dummy = ListNode()
    current = dummy
    
    # Merge using the min-heap
    while min_heap:
        # Pop the node with the smallest value from the heap
        val, node = heapq.heappop(min_heap)
        
        # Append this node to the merged list
        current.next = node
        current = current.next
        
        # Push the next node of the popped node to the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))
    
    # Return the merged list starting from dummy.next
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the mergeKLists function
lists = [
    createLinkedList([1,4,5]),
    createLinkedList([1,3,4]),
    createLinkedList([2,6])
]
merged_list = mergeKLists(lists)
print(linkedListToList(merged_list))  # Output: [1,1,2,3,4,4,5,6]
