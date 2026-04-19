class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mp = defaultdict(int)
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]

                longest = max(mp[num], longest)

        return longest

