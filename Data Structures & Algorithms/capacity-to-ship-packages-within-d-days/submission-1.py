class Solution:

    def shipWithinDays(self, weights, days):

        def can_ship(capacity):

            needed_days = 1
            current_weight = 0

            for weight in weights:

                current_weight += weight

                if current_weight > capacity:

                    needed_days += 1

                    if needed_days > days:
                        return False

                    current_weight = weight

            return True

        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left