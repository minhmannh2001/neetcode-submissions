class Solution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort()

        remove = 0

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:

            # overlap
            if start < prev_end:

                remove += 1

                # giữ interval có end nhỏ hơn
                prev_end = min(prev_end, end)

            else:
                prev_end = end

        return remove