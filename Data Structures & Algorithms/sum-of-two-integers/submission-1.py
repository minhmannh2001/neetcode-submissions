class Solution:
    
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            
            temp = (a ^ b) & MASK
            
            b = ((a & b) << 1) & MASK
            
            a = temp
        
        # Convert back to signed integer
        if a <= MAX_INT:
            return a
        
        return ~(a ^ MASK)