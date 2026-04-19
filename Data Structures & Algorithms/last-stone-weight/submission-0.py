import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert sang max heap bằng cách dùng số âm
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # lớn nhất
            x = -heapq.heappop(stones)  # lớn thứ 2

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0