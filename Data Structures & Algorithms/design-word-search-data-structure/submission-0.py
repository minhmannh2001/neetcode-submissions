class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, idx):
            # điều kiện dừng: đã xử lý hết word
            if idx == len(word):
                return node.is_end

            char = word[idx]

            if char == '.':
                # loop qua TẤT CẢ node con tại vị trí hiện tại
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False

            else:
                # ký tự bình thường → đi thẳng như Trie cũ
                if char not in node.children:
                    return False
                return dfs(node.children[char], idx + 1)

        return dfs(self.root, 0)