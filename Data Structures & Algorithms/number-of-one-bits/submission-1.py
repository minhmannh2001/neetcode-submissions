class Solution:
    
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        # Check all 32 bits
        for i in range(32):
            
            mask = 1 << i
            
            # Check if i-th bit is set
            if n & mask:
                count += 1
        
        return count