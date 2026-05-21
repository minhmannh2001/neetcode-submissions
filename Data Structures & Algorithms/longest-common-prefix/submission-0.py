class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            c = strs[0][i]

            for s in strs:
                if s[i] != c:
                    return strs[0][:i]

        return strs[0][:min_len]