from collections import defaultdict


class FreqStack:

    def __init__(self):

        self.freq = defaultdict(int)

        self.freq_to_values = defaultdict(list)

        self.max_freq = 0

        self.timestamp = 0

    def push(self, val: int) -> None:

        old_freq = self.freq[val]

        new_freq = old_freq + 1

        self.freq[val] = new_freq

        self.timestamp += 1

        self.freq_to_values[new_freq].append(
            (val, self.timestamp)
        )

        self.max_freq = max(
            self.max_freq,
            new_freq
        )

    def pop(self) -> int:

        val, ts = self.freq_to_values[
            self.max_freq
        ].pop()

        self.freq[val] -= 1

        if not self.freq_to_values[self.max_freq]:
            self.max_freq -= 1

        return val