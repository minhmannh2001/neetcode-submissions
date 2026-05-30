from sortedcontainers import SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people = SortedList(people)

        boats = 0

        while people:

            heavy = people.pop()   # người nặng nhất

            remain = limit - heavy

            idx = people.bisect_right(remain) - 1

            if idx >= 0:
                people.pop(idx)

            boats += 1

        return boats