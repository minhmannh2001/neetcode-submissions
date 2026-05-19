class Solution:
    
    def reverseBits(self, n: int) -> int:
        
        res = 0
        
        for i in range(32):
            
            # Extract i-th bit
            bit = (n >> i) & 1
            
            # Place it at reversed position
            if bit:
                res |= (1 << (31 - i))
        
        return res