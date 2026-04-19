from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def diff(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])  # (word, steps)
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            for next_word in word_set:
                if next_word in visited:
                    continue

                if diff(word, next_word) == 1:
                    if next_word == endWord:
                        return steps + 1

                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

        return 0