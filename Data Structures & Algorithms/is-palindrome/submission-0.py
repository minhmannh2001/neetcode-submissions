class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s2 = ""
        for c in s:
            if "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9":
                s1 += c.lower()
                s2 = c.lower() + s2
        return s1 == s2
        