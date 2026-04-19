class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []  # lưu time của từng fleet
        
        for pos, spd in pairs:
            time = (target - pos) / spd
            
            if not stack or time > stack[-1]:
                stack.append(time)
            # time <= stack[-1]: bị chặn, không push
        
        return len(stack)