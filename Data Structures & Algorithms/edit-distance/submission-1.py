class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(cur: str, target: str) -> int:
            if cur == target:
                return 0

            if (cur, target) in memo:
                return memo[(cur, target)]

            # tối ưu nhỏ: nếu 1 bên rỗng
            if not cur:
                return len(target)
            if not target:
                return len(cur)

            res = float("inf")

            # nếu ký tự đầu giống nhau → skip
            if cur[0] == target[0]:
                res = dfs(cur[1:], target[1:])
            else:
                # 🟥 delete
                delete = 1 + dfs(cur[1:], target)

                # 🟩 insert (chèn target[0] vào đầu cur)
                insert = 1 + dfs(target[0] + cur, target)

                # 🟦 replace
                replace = 1 + dfs(target[0] + cur[1:], target)

                res = min(delete, insert, replace)

            memo[(cur, target)] = res
            return res

        return dfs(word1, word2)