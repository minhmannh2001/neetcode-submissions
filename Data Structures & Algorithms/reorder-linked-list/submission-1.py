class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        
        # bước 1: lưu node vào array
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # bước 2: reorder
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            
            if left == right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1
        
        # kết thúc list
        nodes[left].next = None