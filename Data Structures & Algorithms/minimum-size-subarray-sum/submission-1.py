from bisect import bisect_left
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        answer = float("inf")

        for i in range(n):
            need = prefix[i] + target

            k = bisect_left(prefix, need)

            if k <= n:
                answer = min(answer, k - i)

        return 0 if answer == float("inf") else answer