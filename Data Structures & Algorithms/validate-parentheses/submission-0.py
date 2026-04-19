class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # map đóng ngoặc -> mở ngoặc tương ứng
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # nếu là đóng ngoặc
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                # là mở ngoặc
                stack.append(ch)

        return len(stack) == 0