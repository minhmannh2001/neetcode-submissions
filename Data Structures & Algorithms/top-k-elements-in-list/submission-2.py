class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1
        
        heap = []
        for key, value in frequency_dict.items():
            heapq.heappush(heap, (value,  key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for value in heap:
            res.append(value[1])
        
        return res




        