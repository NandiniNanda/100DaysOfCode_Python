class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.buckets[index] is None:
            self.buckets[index] = Node(key, value)
        else:
            current = self.buckets[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        current = prev = self.buckets[index]
        if not current:
            return
        if current.key == key:
            self.buckets[index] = current.next
        else:
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev, current = current, current.next

# Example usage
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))  # Output: 1
print(obj.get(3))  # Output: -1
obj.put(2, 1)
print(obj.get(2))  # Output: 1
obj.remove(2)
print(obj.get(2))  # Output: -1
