class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def check(start):
            current_gas = 0

            for step in range(n):
                i = (start + step) % n

                current_gas += gas[i] - cost[i]

                if current_gas < 0:
                    return False

            return True

        for start in range(n):
            if check(start):
                return start

        return -1