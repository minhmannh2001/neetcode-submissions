class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        counts = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []

        while True:

            counts.sort(reverse=True)

            placed = False

            for item in counts:

                count, ch = item

                if count == 0:
                    continue

                if len(ans) >= 2 and ans[-1] == ans[-2] == ch:
                    continue

                ans.append(ch)
                item[0] -= 1
                placed = True
                break

            if not placed:
                break

        return "".join(ans)