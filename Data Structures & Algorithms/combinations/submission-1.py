class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(start):
            if len(path) == k:
                ans.append(path[:])
                return

            need = k - len(path)

            for num in range(start, n - need + 2):
                path.append(num)
                dfs(num + 1)
                path.pop()

        dfs(1)
        return ans