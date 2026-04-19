from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.i = len(tokens) - 1

        def solve():
            token = tokens[self.i]
            self.i -= 1

            if token not in "+-*/":
                return int(token)

            b = solve()
            a = solve()

            if token == "+":
                return a + b
            if token == "-":
                return a - b
            if token == "*":
                return a * b
            return int(a / b)

        return solve()