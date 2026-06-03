import heapq
from collections import defaultdict


class FreqStack:

    def __init__(self):

        self.freq = defaultdict(int)

        self.heap = []

        self.time = 0

    def push(self, val: int) -> None:

        self.freq[val] += 1

        self.time += 1

        heapq.heappush(
            self.heap,
            (
                -self.freq[val],
                -self.time,
                val
            )
        )

    def pop(self) -> int:

        while True:

            neg_freq, neg_time, val = heapq.heappop(
                self.heap
            )

            freq = -neg_freq

            if self.freq[val] == freq:

                self.freq[val] -= 1

                return val