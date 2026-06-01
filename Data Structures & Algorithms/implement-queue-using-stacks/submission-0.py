class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())

        result = self.s2.pop()

        while self.s2:
            self.s1.append(self.s2.pop())

        return result

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())

        result = self.s2[-1]

        while self.s2:
            self.s1.append(self.s2.pop())

        return result

    def empty(self) -> bool:
        return len(self.s1) == 0