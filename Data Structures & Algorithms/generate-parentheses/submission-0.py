class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate_all(current, length):
            if len(current) == length:
                return [current]
            result = []
            result += generate_all(current + '(', length)
            result += generate_all(current + ')', length)
            return result
        
        def is_valid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0:   # ) xuất hiện trước (
                    return False
            return count == 0   # số ( phải bằng số )
        
        all_strings = generate_all('', 2 * n)
        return [s for s in all_strings if is_valid(s)]