import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda trip: trip[1])

        heap = []

        current_passengers = 0

        for passengers, start, end in trips:

            while heap and heap[0][0] <= start:
                drop_off, num = heapq.heappop(heap)
                current_passengers -= num

            current_passengers += passengers

            if current_passengers > capacity:
                return False

            heapq.heappush(heap, (end, passengers))

        return True