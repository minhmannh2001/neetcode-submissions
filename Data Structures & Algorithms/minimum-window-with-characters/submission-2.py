class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        min_len = float('inf')
        result = ""
        
        # Với mỗi vị trí bắt đầu i
        for i in range(len(s)):
            dict_window = {}  # Đếm tần suất trong window
            
            # Mở rộng window từ i đến j
            for j in range(i, len(s)):
                # Thêm ký tự mới vào window
                char = s[j]
                dict_window[char] = dict_window.get(char, 0) + 1
                
                # Kiểm tra có đủ chưa
                if self.is_valid(dict_window, dict_t):
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        result = s[i:j+1]
                    break  # Đã tìm được substring ngắn nhất bắt đầu từ i
        
        return result
    
    def is_valid(self, dict_window, dict_t):
        for char, count in dict_t.items():
            if dict_window.get(char, 0) < count:
                return False
        return True