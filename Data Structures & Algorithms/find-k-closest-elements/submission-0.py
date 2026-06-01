class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        candidates = []

        for num in arr:
            candidates.append((abs(num - x), num))

        candidates.sort()

        result = []

        for i in range(k):
            result.append(candidates[i][1])

        result.sort()

        return result