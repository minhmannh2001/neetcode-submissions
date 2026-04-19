class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in mapping:
                stack.append(mapping[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False

        return not stack