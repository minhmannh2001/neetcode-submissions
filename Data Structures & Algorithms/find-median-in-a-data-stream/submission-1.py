class MedianFinder:

    def __init__(self):
        self.max_heap = []   # nửa trái
        self.min_heap = []   # nửa phải

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        # đảm bảo mọi phần tử trái ≤ phải
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # cân bằng: max_heap nhiều hơn tối đa 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return float(-self.max_heap[0])  # max_heap nhiều hơn