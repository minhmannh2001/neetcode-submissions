import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)       # dùng luôn add để init

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # Giữ heap đúng k phần tử
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)    # bỏ phần tử nhỏ nhất

        return self.heap[0]             # min của heap = kth largest