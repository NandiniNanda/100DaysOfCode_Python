class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Example usage:
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # Output: True
print(myCircularQueue.enQueue(2))  # Output: True
print(myCircularQueue.enQueue(3))  # Output: True
print(myCircularQueue.enQueue(4))  # Output: False
print(myCircularQueue.Rear())      # Output: 3
print(myCircularQueue.isFull())    # Output: True
print(myCircularQueue.deQueue())   # Output: True
print(myCircularQueue.enQueue(4))  # Output: True
print(myCircularQueue.Rear())      # Output: 4
