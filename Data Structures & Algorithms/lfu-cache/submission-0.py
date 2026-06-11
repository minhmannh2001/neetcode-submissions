class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}
        self.freq = {}
        self.last_used = {}

        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.time += 1

        self.freq[key] += 1
        self.last_used[key] = self.time

        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        self.time += 1

        if key in self.cache:
            self.cache[key] = value

            self.freq[key] += 1
            self.last_used[key] = self.time
            return

        if len(self.cache) == self.capacity:

            victim = None

            for k in self.cache:

                if victim is None:
                    victim = k
                    continue

                if self.freq[k] < self.freq[victim]:
                    victim = k

                elif self.freq[k] == self.freq[victim]:
                    if self.last_used[k] < self.last_used[victim]:
                        victim = k

            del self.cache[victim]
            del self.freq[victim]
            del self.last_used[victim]

        self.cache[key] = value
        self.freq[key] = 1
        self.last_used[key] = self.time