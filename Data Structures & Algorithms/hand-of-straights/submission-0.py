class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        # không chia đều được
        if n % groupSize != 0:
            return False

        hand.sort()

        num_groups = n // groupSize

        groups = [[] for _ in range(num_groups)]

        for card in hand:
            placed = False

            # thử đặt card vào từng group
            for group in groups:

                # group đã đầy
                if len(group) == groupSize:
                    continue

                # group rỗng -> add luôn
                if not group:
                    group.append(card)
                    placed = True
                    break

                # phải consecutive
                if group[-1] + 1 == card:
                    group.append(card)
                    placed = True
                    break

            # không đặt được vào đâu
            if not placed:
                return False

        # mọi group phải đủ size
        for group in groups:
            if len(group) != groupSize:
                return False

        return True