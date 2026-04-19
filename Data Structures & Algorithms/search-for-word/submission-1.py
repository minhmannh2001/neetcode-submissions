class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, idx):
            # điều kiện dừng: tìm được hết word
            if idx == len(word):
                return True

            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # ô đã dùng rồi
            if (r, c) in visited:
                return False

            # ký tự không khớp
            if board[r][c] != word[idx]:
                return False

            # đánh dấu đang dùng ô này
            visited.add((r, c))

            # tìm 4 ô xung quanh với ký tự tiếp theo
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))

            # SAU KHI đệ quy xong, phải bỏ visited!
            # để các path khác có thể dùng lại ô này
            # ví dụ:
            #   path 1: A→B→C (thất bại)
            #   path 2: muốn dùng lại ô A
            #   → nếu không remove, path 2 sẽ bỏ lỡ ô A
            visited.remove((r, c))

            return found

        # loop qua tất cả ký tự theo hàng rồi cột
        # tìm ký tự đầu tiên của word để bắt đầu dfs
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False