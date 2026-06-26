from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        arr = []

        for i, (enqueue, process) in enumerate(tasks):
            arr.append((enqueue, process, i))

        arr.sort()

        heap = []

        ans = []

        current = 0

        i = 0

        n = len(arr)

        while i < n or heap:

            if not heap:
                current = max(current, arr[i][0])

            while i < n and arr[i][0] <= current:
                enqueue, process, idx = arr[i]
                heappush(heap, (process, idx))
                i += 1

            process, idx = heappop(heap)

            current += process

            ans.append(idx)

        return ans