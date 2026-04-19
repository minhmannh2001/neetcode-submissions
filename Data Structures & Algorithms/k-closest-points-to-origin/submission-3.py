class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0]**2 + p[1]**2

        def partition(left, right):
            pivot = dist(points[right])
            i = left
            for j in range(left, right):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i

        left, right = 0, len(points) - 1
        while left <= right:
            pivotIdx = partition(left, right)
            if pivotIdx == k:
                break
            elif pivotIdx < k:
                left = pivotIdx + 1
            else:
                right = pivotIdx - 1

        return points[:k]