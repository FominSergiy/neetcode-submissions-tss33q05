from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # SORT FIRST
        # intervals.sort(key=lambda item: item[0])
        # output = [intervals[0]]
        # # look forward to an overlapping interval, but sort first

        # for start, end in intervals:
        #     last_end = output[-1][1]
        #     if last_end >= start: # overlap
        #         output[-1][1] = max(output[-1][1], end)
        #         output[-1][0] = min(output[-1][0], start)
        #     else:
        #         output.append([start, end])
        
        # return output

        # SWEEP LINE ALGO
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []
        interval = []
        have = 0
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        
        return res
