class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    nodes = []
    for linked_list in lists:
        while linked_list:
            nodes.append(linked_list.val)
            linked_list = linked_list.next
    nodes.sort()
    
    dummy = ListNode()
    current = dummy
    for node_val in nodes:
        current.next = ListNode(node_val)
        current = current.next
    
    return dummy.next

# Function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Take user input for the number of lists
num_lists = int(input("Enter the number of linked lists: "))

# Take user input for each linked list
lists = []
for i in range(num_lists):
    input_str = input(f"Enter the space-separated values for linked list {i + 1}: ")
    values = list(map(int, input_str.split()))
    linked_list = createLinkedList(values)
    lists.append(linked_list)

# Merge the linked lists
merged_list = mergeKLists(lists)

# Print the merged linked list
print("Merged linked list:")
printLinkedList(merged_list)
