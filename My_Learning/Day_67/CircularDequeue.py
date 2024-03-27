class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.val if self.size > 0 else -1

    def getRear(self) -> int:
        return self.tail.prev.val if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Example usage:
myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  # Output: True
print(myCircularDeque.insertLast(2))  # Output: True
print(myCircularDeque.insertFront(3)) # Output: True
print(myCircularDeque.insertFront(4)) # Output: False
print(myCircularDeque.getRear())      # Output: 2
print(myCircularDeque.isFull())       # Output: True
print(myCircularDeque.deleteLast())   # Output: True
print(myCircularDeque.insertFront(4)) # Output: True
print(myCircularDeque.getFront())     # Output: 4
