"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        s = 0
        e = 0

        count = 0
        result = 0

        while s < len(intervals):

            # meeting mới bắt đầu trước khi meeting cũ kết thúc
            if start[s] < end[e]:

                count += 1
                result = max(result, count)

                s += 1

            # có meeting kết thúc -> free room
            else:

                count -= 1
                e += 1

        return result