from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map  = {}                           # key → [value, freq]
        self.freq_map = defaultdict(OrderedDict)     # freq → OrderedDict{key: None}

    def _increment(self, key: int):
        value, freq = self.key_map[key]

        # xoá key khỏi bucket freq cũ
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:                  # bucket rỗng thì dọn
            del self.freq_map[freq]
            if self.min_freq == freq:                # nếu đây là min_freq thì tăng lên
                self.min_freq += 1

        # thêm key vào bucket freq mới
        new_freq = freq + 1
        self.key_map[key] = [value, new_freq]
        self.freq_map[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        self._increment(key)
        return self.key_map[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            self.key_map[key][0] = value             # cập nhật value
            self._increment(key)
            return

        # cache đầy → xoá LFU (và LRU nếu tie)
        if len(self.key_map) == self.capacity:
            lru_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[lru_key]

        # insert key mới, freq = 1
        self.key_map[key] = [value, 1]
        self.freq_map[1][key] = None
        self.min_freq = 1