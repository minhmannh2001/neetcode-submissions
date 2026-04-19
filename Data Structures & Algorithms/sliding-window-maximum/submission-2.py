from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # Lưu index, giá trị giảm dần
        
        for i in range(len(nums)):
            # Bước 1: Loại bỏ index ngoài window
            # Window hiện tại: [i-k+1, i]
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Bước 2: Loại bỏ các phần tử nhỏ hơn nums[i]
            # Duy trì tính giảm dần trong deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Bước 3: Thêm index hiện tại vào deque
            dq.append(i)
            
            # Bước 4: Lưu kết quả khi window đủ k phần tử
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result