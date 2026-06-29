from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)

        path = []

        n = len(s)

        def dfs():

            remaining = n - len(path)

            if max(counter.values(), default=0) > (remaining + 1) // 2:
                return False

            if len(path) == n:
                return True

            for ch in sorted(counter, key=lambda x: -counter[x]):

                if counter[ch] == 0:
                    continue

                if path and path[-1] == ch:
                    continue

                counter[ch] -= 1
                path.append(ch)

                if dfs():
                    return True

                path.pop()
                counter[ch] += 1

            return False

        if dfs():
            return "".join(path)

        return ""