class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(idx: int, current: str):
            # điều kiện dừng: đã xử lý hết các digit
            if idx == len(digits):
                result.append(current)
                return

            # thử từng chữ cái của digit hiện tại
            for char in phone_map[digits[idx]]:
                backtrack(idx + 1, current + char)

        backtrack(0, '')
        return result