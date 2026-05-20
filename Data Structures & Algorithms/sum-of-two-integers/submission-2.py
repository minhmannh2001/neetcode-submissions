class Solution:
    
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        res = 0
        carry = 0
        
        for i in range(32):
            
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            
            # Sum bit
            current = a_bit ^ b_bit ^ carry
            
            if current:
                res |= (1 << i)
            
            # Compute new carry
            carry = (
                (a_bit & b_bit)
                | (a_bit & carry)
                | (b_bit & carry)
            )
        
        # Convert to signed integer
        if res <= MAX_INT:
            return res
        
        return ~(res ^ MASK)