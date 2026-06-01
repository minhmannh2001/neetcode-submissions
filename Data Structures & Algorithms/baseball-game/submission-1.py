class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                total += score

            elif op == "D":
                score = stack[-1] * 2
                stack.append(score)
                total += score

            elif op == "C":
                score = stack.pop()
                total -= score

            else:
                score = int(op)
                stack.append(score)
                total += score

        return total