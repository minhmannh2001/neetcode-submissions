class Solution:
    def checkValidString(self, s: str) -> bool:

        left_stack = []
        star_stack = []

        for i, c in enumerate(s):

            if c == '(':
                left_stack.append(i)

            elif c == '*':
                star_stack.append(i)

            else:  # ')'

                if left_stack:
                    left_stack.pop()

                elif star_stack:
                    star_stack.pop()

                else:
                    return False

        # match remaining '(' with '*'
        while left_stack and star_stack:

            left_index = left_stack.pop()
            star_index = star_stack.pop()

            # '*' must be after '('
            if left_index > star_index:
                return False

        return len(left_stack) == 0