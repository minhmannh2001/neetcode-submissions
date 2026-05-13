from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # Sort intervals by start
        intervals.sort()
        
        # Store original index before sorting queries
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        
        # Min heap:
        # (interval_size, interval_end)
        heap = []
        
        interval_idx = 0
        
        for q, original_idx in sorted_queries:
            
            # Add all intervals whose start <= current query
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= q:
                
                left, right = intervals[interval_idx]
                
                interval_size = right - left + 1
                
                heapq.heappush(heap, (interval_size, right))
                
                interval_idx += 1
            
            # Remove intervals that cannot contain q anymore
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # Top of heap = smallest valid interval
            if heap:
                res[original_idx] = heap[0][0]
        
        return res