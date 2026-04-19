class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # dummy head & tail
        self.head = Node(0, 0)  # LRU side
        self.tail = Node(0, 0)  # MRU side

        self.head.next = self.tail
        self.tail.prev = self.head

    # remove node khỏi linked list
    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # add node vào cuối (MRU)
    def _add(self, node: Node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # move node lên MRU
        self._remove(node)
        self._add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            # move lên MRU
            self._remove(node)
            self._add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)

            # nếu vượt capacity → xoá LRU
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]