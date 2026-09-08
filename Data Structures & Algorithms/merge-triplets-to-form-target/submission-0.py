class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 2 ways to slove
        # for each triplet, as long as triplet[i] is not > target we can consider it
        # track set of 3 idx that we then return
        good = set()

        for t in triplets:
            if (
                t[0] > target[0] or
                t[1] > target[1] or
                t[2] > target[2]
            ):
                continue # do not consider this triplet
            for idx, val in enumerate(t):
                if val == target[idx]:
                    good.add(idx)
        
        return len(good) == 3