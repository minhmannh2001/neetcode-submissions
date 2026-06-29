from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)

        heap = []

        for ch, freq in counter.items():
            heapq.heappush(heap, (-freq, ch))

        ans = []

        prev_freq = 0
        prev_char = ""

        while heap:

            freq, ch = heapq.heappop(heap)

            ans.append(ch)

            freq += 1

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_freq = freq
            prev_char = ch

        if len(ans) != len(s):
            return ""

        return "".join(ans)