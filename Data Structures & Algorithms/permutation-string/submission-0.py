class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        for start in range(len2 - len1 + 1):
            substring = s2[start:start + len1]

            # Tạo bản sao để check
            temp = list(s1)

            valid = True

            for char in substring:
                if char in temp:
                    temp.remove(char)
                else:
                    valid = False
                    break

            if valid:
                return True

        return False
