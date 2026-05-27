class Solution:
    def validPalindrome(self, s: str) -> bool:

        def dfs(i, j, deleted):

            while i < j:

                if s[i] != s[j]:

                    if deleted:
                        return False

                    return (
                        dfs(i + 1, j, True) or
                        dfs(i, j - 1, True)
                    )

                i += 1
                j -= 1

            return True

        return dfs(0, len(s) - 1, False)