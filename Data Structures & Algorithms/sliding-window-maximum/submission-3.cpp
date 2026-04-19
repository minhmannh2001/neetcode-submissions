#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> dq;  // Lưu index
        
        for (int i = 0; i < nums.size(); i++) {
            // Bước 1: Loại bỏ index ngoài window
            if (!dq.empty() && dq.front() < i - k + 1) {
                dq.pop_front();
            }
            
            // Bước 2: Loại bỏ phần tử nhỏ hơn nums[i]
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            
            // Bước 3: Thêm index hiện tại
            dq.push_back(i);
            
            // Bước 4: Lưu kết quả khi window đủ k phần tử
            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }
        
        return result;
    }
};