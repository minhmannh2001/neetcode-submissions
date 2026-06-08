class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0

        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)

        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = self.front.next
        self.size -= 1

        if self.size == 0:
            self.rear = None

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity