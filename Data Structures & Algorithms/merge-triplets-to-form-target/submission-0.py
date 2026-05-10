class Solution:
    def mergeTriplets(self, triplets, target):
        x, y, z = target

        found_x = found_y = found_z = False

        for a, b, c in triplets:

            # invalid
            if a > x or b > y or c > z:
                continue

            if a == x:
                found_x = True

            if b == y:
                found_y = True

            if c == z:
                found_z = True

        return found_x and found_y and found_z