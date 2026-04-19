class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Đếm tần suất ký tự trong t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        min_len = float('inf')
        result = ""
        
        # Thử tất cả substring (i, j)
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                
                # Kiểm tra substring này có chứa đủ ký tự của t không
                if self.contains_all(substring, dict_t):
                    if len(substring) < min_len:
                        min_len = len(substring)
                        result = substring
        
        return result
    
    def contains_all(self, substring, dict_t):
        """Kiểm tra substring có chứa đủ tất cả ký tự của t không"""
        # Đếm tần suất trong substring
        dict_sub = {}
        for char in substring:
            dict_sub[char] = dict_sub.get(char, 0) + 1
        
        # So sánh với dict_t
        for char, count in dict_t.items():
            if dict_sub.get(char, 0) < count:
                return False
        
        return True