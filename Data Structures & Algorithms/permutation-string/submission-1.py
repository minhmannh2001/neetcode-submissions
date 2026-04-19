class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        # Count frequency of s1
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        # Check each substring
        for start in range(len2 - len1 + 1):
            count2 = [0] * 26

            for i in range(len1):
                count2[ord(s2[start + i]) - ord('a')] += 1

            if count1 == count2:
                return True

        return False
