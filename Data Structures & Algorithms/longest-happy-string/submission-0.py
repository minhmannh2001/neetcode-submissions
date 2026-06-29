from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        heap = []

        if a:
            heappush(heap, (-a, 'a'))
        if b:
            heappush(heap, (-b, 'b'))
        if c:
            heappush(heap, (-c, 'c'))

        ans = []

        while heap:

            count1, ch1 = heappop(heap)

            # Nếu thêm ký tự này sẽ tạo xxx
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:

                if not heap:
                    break

                count2, ch2 = heappop(heap)

                ans.append(ch2)
                count2 += 1          # vì count đang âm

                if count2 < 0:
                    heappush(heap, (count2, ch2))

                heappush(heap, (count1, ch1))

            else:

                ans.append(ch1)
                count1 += 1

                if count1 < 0:
                    heappush(heap, (count1, ch1))

        return "".join(ans)