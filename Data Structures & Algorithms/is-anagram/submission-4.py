class Solution:
    def convert_string_to_anagram_format(self, s: str) -> dict:
        anagram_format = {
            'len': len(s),
            'unique_chars': sorted(list(s))
        }
        return anagram_format
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_format_s = self.convert_string_to_anagram_format(s)
        anagram_format_t = self.convert_string_to_anagram_format(t)
        if anagram_format_s == anagram_format_t:
            return True
        else:
            return False