"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        # sort theo start time
        intervals.sort(key=lambda interval: interval.start)

        # min heap lưu end times của các room đang dùng
        heap = []

        # meeting đầu tiên dùng room đầu tiên
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):

            current_start = intervals[i].start
            current_end = intervals[i].end

            # nếu room kết thúc sớm nhất đã free
            if current_start >= heap[0]:
                heapq.heappop(heap)

            # dùng room (cũ hoặc mới)
            heapq.heappush(heap, current_end)

        return len(heap)