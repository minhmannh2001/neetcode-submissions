class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        def dfs(cards):
            # hết bài
            if not cards:
                return True

            start = cards[0]

            new_cards = cards[:]

            # cố build 1 group
            for x in range(start, start + groupSize):

                if x not in new_cards:
                    return False

                new_cards.remove(x)

            return dfs(new_cards)

        return dfs(hand)