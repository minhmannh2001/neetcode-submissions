class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        hand.sort()

        for x in hand:

            # đã dùng hết
            if count[x] == 0:
                continue

            # build group
            for num in range(x, x + groupSize):

                if count[num] == 0:
                    return False

                count[num] -= 1

        return True