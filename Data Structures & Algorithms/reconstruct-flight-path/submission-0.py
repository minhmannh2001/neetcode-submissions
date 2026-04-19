from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # build graph, sort để lexicographically nhỏ nhất
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        # reverse=True khi build → dùng pop() lấy nhỏ nhất O(1)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            result.append(airport)   # thêm vào khi không đi tiếp được

        dfs("JFK")
        return result[::-1]          # reverse lại vì thêm ngược