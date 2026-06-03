class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for part in path.split("/"):

            # Bỏ qua:
            # ""
            # "."
            if part == "" or part == ".":
                continue

            # Quay về thư mục cha
            elif part == "..":

                if stack:
                    stack.pop()

            # Tên thư mục hợp lệ
            else:
                stack.append(part)

        return "/" + "/".join(stack)