class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # không đủ tổng xăng
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # fail tại i
            if tank < 0:
                start = i + 1
                tank = 0

        return start