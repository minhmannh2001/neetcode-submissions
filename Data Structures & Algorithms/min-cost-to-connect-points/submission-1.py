class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        # dist[i] = chi phí rẻ nhất để kéo point i vào MST
        dist = [float('inf')] * n
        dist[0] = 0   # bắt đầu từ point 0
        total = 0

        while len(visited) < n:
            # tìm point chưa visited có dist nhỏ nhất (thay cho heappop)
            i = -1
            for j in range(n):
                if j not in visited:
                    if i == -1 or dist[j] < dist[i]:
                        i = j

            visited.add(i)
            total += dist[i]

            # update dist của các point chưa visited
            for j in range(n):
                if j not in visited:
                    d = abs(points[i][0] - points[j][0]) + \
                        abs(points[i][1] - points[j][1])
                    dist[j] = min(dist[j], d)   # ghi đè nếu rẻ hơn

        return total