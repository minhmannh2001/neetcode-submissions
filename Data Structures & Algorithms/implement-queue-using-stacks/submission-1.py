class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack.pop()

        if not self.stack:
            return x

        result = self.pop()

        self.stack.append(x)

        return result

    def peek(self) -> int:
        x = self.stack.pop()

        if not self.stack:
            self.stack.append(x)
            return x

        result = self.peek()

        self.stack.append(x)

        return result

    def empty(self) -> bool:
        return len(self.stack) == 0