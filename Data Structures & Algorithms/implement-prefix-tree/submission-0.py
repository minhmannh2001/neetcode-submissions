class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False  # có word kết thúc tại đây không


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # tạo node mới nếu chưa có
            node = node.children[char]             # đi xuống node con
        node.is_end = True                         # đánh dấu kết thúc word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False          # ký tự không tồn tại → False
            node = node.children[char]
        return node.is_end            # phải là kết thúc word, không chỉ prefix

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True    