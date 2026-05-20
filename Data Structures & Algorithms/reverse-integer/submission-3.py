class Solution:
    
    def reverse(self, x: int) -> int:
        
        MIN_INT = -(2 ** 31)
        MAX_INT = (2 ** 31) - 1
        
        sign = -1 if x < 0 else 1
        
        s = str(abs(x))
        
        reversed_num = int(s[::-1]) * sign
        
        if reversed_num < MIN_INT or reversed_num > MAX_INT:
            return 0
        
        return reversed_num