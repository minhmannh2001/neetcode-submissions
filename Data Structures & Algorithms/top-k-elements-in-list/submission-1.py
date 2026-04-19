class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for num in nums:
            frequency_dict[num] += 1
        sorted_frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_frequency_dict.keys())[:k]




        