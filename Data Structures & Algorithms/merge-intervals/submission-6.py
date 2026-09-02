from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # SORT FIRST
        # intervals.sort(key=lambda item: item[0])
        # output = [intervals[0]]
        
        # for start, end in intervals[1:]:
        #     if output[-1][1] < start:
        #         output.append([start, end])
        #     else:
        #         output[-1][0] = min(output[-1][0], start)
        #         output[-1][1] = max(output[-1][1], end)
        # return output
        # SWEEP LINE ALGO
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        output = []
        interval = []
        have = 0

        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            # boudary found
            if have == 0:
                interval.append(i)
                output.append(interval)
                interval = []
        return output