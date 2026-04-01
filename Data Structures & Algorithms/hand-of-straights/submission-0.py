class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # map {1: 1, 2:1, 3:2, 4:1, 5:1, 6:1, 7:1}

        # 1, 2, 3, 3, 4, 5, 6, 7

        # 1, 2, 3, 4
        # {3:1, 5:1, 6:1, 7: 1}

        # 3, 4??
        # {5:1, 6:1, 7: 1}

        # -> False

        count = Counter(hand)
        hand.sort()

        for card in hand:
            if count[card]:
                for i in range(card, card+groupSize):
                    if i not in count:
                        return False
                    count[i] -= 1

        return True
