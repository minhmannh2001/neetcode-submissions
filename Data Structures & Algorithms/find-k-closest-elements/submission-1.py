class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        # Tìm vị trí chèn của x
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2

            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        pos = left

        left = pos - 1
        right = pos

        # Mở rộng cửa sổ đến khi có k phần tử
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= n:
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]