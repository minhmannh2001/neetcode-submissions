import string
import random

class Solution:

    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits  # All letters (upper/lower) and digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def encode(self, strs: List[str]) -> str:
        secret_delimiter = self.generate_random_string(6)
        encoded_str = secret_delimiter
        for s in strs:
            encoded_str += s + secret_delimiter
        return encoded_str

    def decode(self, s: str) -> List[str]:
        secret_delimiter = s[:6]
        strs = s.split(secret_delimiter)
        strs = strs[1:-1]
        return strs


