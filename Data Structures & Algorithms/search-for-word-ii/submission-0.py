class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # lưu word hoàn chỉnh tại node kết thúc


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Bước 1: insert tất cả words vào Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word   # lưu word tại node cuối

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            # ký tự hiện tại không có trong trie → dừng
            if char not in node.children:
                return

            next_node = node.children[char]

            # tìm thấy word hoàn chỉnh!
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # tránh duplicate

            # đánh dấu đã dùng
            board[r][c] = '#'

            # đi 4 hướng
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # restore
            board[r][c] = char

        # Bước 2: DFS từng ô trên board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result