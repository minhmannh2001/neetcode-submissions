class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        result = []

        def generate(start: int, current: List[str]):
            # điều kiện dừng: đã cắt hết string
            if start == len(s):
                result.append(current[:])
                return

            # thử mọi điểm cắt từ start đến cuối
            for end in range(start, len(s)):
                substring = s[start:end+1]

                # chỉ đệ quy tiếp nếu substring hiện tại là palindrome
                if is_palindrome(substring):
                    current.append(substring)
                    generate(end + 1, current)  # cắt tiếp từ sau điểm cắt
                    current.pop()               # backtrack

        generate(0, [])
        return result