func maxSlidingWindow(nums []int, k int) []int {
    n := len(nums)
    if n == 0 || k == 0 {
        return []int{}
    }
    
    result := make([]int, 0, n-k+1)  // Preallocate capacity
    dq := make([]int, 0, n)          // Deque lưu index
    
    for i := 0; i < n; i++ {
        // Bước 1: Loại bỏ index ngoài window
        if len(dq) > 0 && dq[0] < i-k+1 {
            dq = dq[1:]  // Remove first element
        }
        
        // Bước 2: Loại bỏ phần tử nhỏ hơn nums[i]
        for len(dq) > 0 && nums[dq[len(dq)-1]] < nums[i] {
            dq = dq[:len(dq)-1]  // Remove last element
        }
        
        // Bước 3: Thêm index hiện tại
        dq = append(dq, i)
        
        // Bước 4: Lưu kết quả khi window đủ k phần tử
        if i >= k-1 {
            result = append(result, nums[dq[0]])
        }
    }
    
    return result
}