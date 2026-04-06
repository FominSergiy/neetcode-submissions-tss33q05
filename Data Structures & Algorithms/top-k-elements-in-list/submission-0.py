from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        arr = []
        # break from k:v format to [int, int] format - easier to traverse
        for num, cnt in counter.items():
            arr.append([cnt, num])
        arr.sort()

        # since its sorted in ASC order, we pop k items from right
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

        
        