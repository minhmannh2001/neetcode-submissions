class Solution:
    def findMaximizedCapital(self, k: int, w: int,
                             profits: List[int],
                             capital: List[int]) -> int:

        projects = sorted(zip(capital, profits))

        n = len(projects)
        idx = 0
        used = [False] * n

        for _ in range(k):

            # mở khóa các project đủ vốn
            while idx < n and projects[idx][0] <= w:
                idx += 1

            best = -1
            best_profit = -1

            # chỉ tìm trong vùng đã mở khóa
            for i in range(idx):
                if not used[i] and projects[i][1] > best_profit:
                    best_profit = projects[i][1]
                    best = i

            if best == -1:
                break

            used[best] = True
            w += best_profit

        return w