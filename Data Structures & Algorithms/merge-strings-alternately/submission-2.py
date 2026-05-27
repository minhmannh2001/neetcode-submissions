class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = len(word1)
        m = len(word2)

        result = [""] * (n + m)

        i = j = k = 0

        while i < n and j < m:

            result[k] = word1[i]
            k += 1
            i += 1

            result[k] = word2[j]
            k += 1
            j += 1

        while i < n:
            result[k] = word1[i]
            k += 1
            i += 1

        while j < m:
            result[k] = word2[j]
            k += 1
            j += 1

        return "".join(result)