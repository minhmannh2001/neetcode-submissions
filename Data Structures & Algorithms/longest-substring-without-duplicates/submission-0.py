class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_sub_string = ""
        longest_sub_string = ""

        for char in s:
            if char not in current_sub_string:
                # chưa có -> nối vào cuối
                current_sub_string += char
            else:
                # đã có -> cắt chuỗi
                idx = current_sub_string.index(char)
                # cắt từ sau vị trí trùng, rồi nối char hiện tại
                current_sub_string = current_sub_string[idx + 1:] + char

            # cập nhật chuỗi dài nhất
            if len(current_sub_string) > len(longest_sub_string):
                longest_sub_string = current_sub_string

        return len(longest_sub_string)
