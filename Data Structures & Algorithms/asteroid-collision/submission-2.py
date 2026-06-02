from typing import List


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if not asteroids:
            return []

        # Build doubly linked list
        nodes = [Node(x) for x in asteroids]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        head = nodes[0]

        current = head

        while current and current.next:

            left = current
            right = current.next

            # Collision candidate
            if left.value > 0 and right.value < 0:

                left_size = abs(left.value)
                right_size = abs(right.value)

                # Left explodes
                if left_size < right_size:

                    prev_node = left.prev
                    next_node = right

                    if prev_node:
                        prev_node.next = next_node
                    else:
                        head = next_node

                    next_node.prev = prev_node

                    current = prev_node if prev_node else next_node

                # Right explodes
                elif left_size > right_size:

                    next_node = right.next

                    left.next = next_node

                    if next_node:
                        next_node.prev = left

                    current = left

                # Both explode
                else:

                    prev_node = left.prev
                    next_node = right.next

                    if prev_node:
                        prev_node.next = next_node
                    else:
                        head = next_node

                    if next_node:
                        next_node.prev = prev_node

                    current = prev_node if prev_node else next_node

            else:
                current = current.next

        # Convert linked list back to array
        result = []

        node = head

        while node:
            result.append(node.value)
            node = node.next

        return result