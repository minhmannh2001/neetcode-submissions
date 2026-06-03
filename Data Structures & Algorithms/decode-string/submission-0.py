class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        while True:

            changed = False

            for i, ch in enumerate(s):

                if ch == '[':
                    stack.append(i)

                elif ch == ']':

                    changed = True

                    left = stack.pop()

                    # Chuỗi bên trong [...]
                    inner = s[left + 1:i]

                    # Tìm số đứng trước '['
                    j = left - 1

                    while j >= 0 and s[j].isdigit():
                        j -= 1

                    repeat = int(s[j + 1:left])

                    expanded = inner * repeat

                    # Thay thế k[xxx] bằng chuỗi đã decode
                    s = (
                        s[:j + 1]
                        + expanded
                        + s[i + 1:]
                    )

                    break

            if not changed:
                break

        return s