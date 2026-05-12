class Solution:
    def merge(self, intervals):

        # sort theo start
        intervals.sort(key=lambda x: x[0])

        result = []

        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:

            # overlap
            if start <= current_end:

                current_end = max(current_end, end)

            # không overlap
            else:

                result.append([current_start, current_end])

                current_start = start
                current_end = end

        # append interval cuối
        result.append([current_start, current_end])

        return result