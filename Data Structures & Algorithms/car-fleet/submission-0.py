class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Ghép position và speed lại, sort theo position giảm dần
        pairs = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0  # time của fleet đang dẫn đầu (gần đích nhất chưa bị chặn)
        
        for pos, spd in pairs:
            time = (target - pos) / spd
            
            if time > max_time:
                # Xe này không đuổi kịp fleet phía trước → tạo fleet mới
                fleets += 1
                max_time = time
            # Nếu time <= max_time: xe này bị chặn, cùng fleet với xe trước
        
        return fleets