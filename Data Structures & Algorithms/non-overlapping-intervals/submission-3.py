class Solution:
    def eraseOverlapIntervals(self, intervals):

        intervals.sort()

        n = len(intervals)

        memo = {}

        def dfs(i, prev):

            if i == n:
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            # không overlap
            if intervals[i][0] >= intervals[prev][1]:

                ans = dfs(i + 1, i)

            else:

                # remove current
                option1 = 1 + dfs(i + 1, prev)

                # remove previous
                option2 = 1 + dfs(i + 1, i)

                ans = min(option1, option2)

            memo[(i, prev)] = ans

            return ans

        return dfs(1, 0)