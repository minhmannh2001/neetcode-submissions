class Solution:
    def insert(self, intervals, newInterval):

        result = []

        for i in range(len(intervals)):

            start, end = intervals[i]

            # interval nằm hoàn toàn bên trái
            if end < newInterval[0]:
                result.append([start, end])

            # newInterval nằm hoàn toàn bên trái
            elif newInterval[1] < start:

                result.append(newInterval)

                # append phần còn lại
                result.extend(intervals[i:])

                return result

            # overlap
            else:

                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        # nếu merge tới cuối hoặc insert ở cuối
        result.append(newInterval)

        return result