class Solution:
    
    def countBits(self, n: int) -> List[int]:
        
        def count_ones(x):
            
            count = 0
            
            while x:
                count += x & 1
                x >>= 1
            
            return count
        
        res = []
        
        for i in range(n + 1):
            res.append(count_ones(i))
        
        return res