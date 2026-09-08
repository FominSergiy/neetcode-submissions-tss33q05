from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hands should be equally divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        # idea is, we want to get a sequence of int of groupSize
        # and as long as we have in there, we sequence is valid
        # the moment we are missing a number, we can safely exit - cannot build the sequence
        # counter = Counter(hand)
        # hand.sort()

        # since counter stores actual numbers, do not iterate using idx
        # but actual numbers
        # but make sure they are sorted asc
        # for num in hand:
        #     if counter[num]:
        #         for i in range(num, num + groupSize):
        #             if not counter[i]:
        #                 return False
        #             counter[i] -= 1
        # return True
        
        counter = Counter(hand)
        for num in hand:
            start = num
            while counter[start - 1]:
                start -= 1
            while start <= num: # guard for the current range of groupSize
                while counter[start]:
                    for i in range(start, start + groupSize):
                        if not counter[i]:
                            return False
                        counter[i] -= 1
                start += 1
        return True