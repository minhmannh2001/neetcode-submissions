from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # (cnt, available_at)

        while max_heap or queue:
            time += 1

            if not max_heap:
                # nhảy thẳng đến task gần nhất
                time = queue[0][1]

            # trả task hết cooldown về heap TRƯỚC khi pop
            while queue and queue[0][1] <= time:
                heapq.heappush(max_heap, queue[0][0])
                queue.popleft()

            cnt = heapq.heappop(max_heap) + 1
            if cnt < 0:
                queue.append((cnt, time + n + 1))

        return time