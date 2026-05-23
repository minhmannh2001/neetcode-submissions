class MyHashMap:

    def __init__(self):

        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]


    def hash(self, key: int) -> int:
        return key % self.size


    def put(self, key: int, value: int) -> None:

        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):

            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))


    def get(self, key: int) -> int:

        index = self.hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:

            if k == key:
                return v

        return -1


    def remove(self, key: int) -> None:

        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):

            if k == key:
                bucket.pop(i)
                return