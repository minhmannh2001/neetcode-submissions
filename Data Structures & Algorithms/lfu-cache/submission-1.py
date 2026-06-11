from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_to_tail(self, node):

        prev_tail = self.tail.prev

        prev_tail.next = node
        node.prev = prev_tail

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def pop_front(self):

        if self.size == 0:
            return None

        node = self.head.next
        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0

        self.min_freq = 0

        self.nodes = {}

        self.freq_map = defaultdict(DoublyLinkedList)

    def _increase_freq(self, node):

        old_freq = node.freq

        self.freq_map[old_freq].remove(node)

        if (
            old_freq == self.min_freq
            and self.freq_map[old_freq].size == 0
        ):
            self.min_freq += 1

        node.freq += 1

        self.freq_map[node.freq].add_to_tail(node)

    def get(self, key: int) -> int:

        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        self._increase_freq(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.nodes:

            node = self.nodes[key]
            node.value = value

            self._increase_freq(node)

            return

        if self.size == self.capacity:

            victim = self.freq_map[self.min_freq].pop_front()

            del self.nodes[victim.key]

            self.size -= 1

        node = Node(key, value)

        self.nodes[key] = node

        self.freq_map[1].add_to_tail(node)

        self.min_freq = 1

        self.size += 1