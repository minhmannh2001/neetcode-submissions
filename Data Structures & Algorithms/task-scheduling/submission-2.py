class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        freq_max = max(freq.values())

        # đếm bao nhiêu task có tần số bằng max
        count_max = sum(1 for v in freq.values() if v == freq_max)

        formula = (freq_max - 1) * (n + 1) + count_max

        return max(formula, len(tasks))