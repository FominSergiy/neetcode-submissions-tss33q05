class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[0])
        last_e = intervals[0][1]
        remove = 0
        for start, end in intervals[1:]:
            if last_e <= start:
                last_e = end
            else:
                last_e = min(end, last_e)
                remove += 1
        return remove
        # greedy local choices
        # 1 - for interval[i] if  no overlap with previous end
        # set prev end to this end

        # 2. otherwise there is overlap
        # keep the shorter interval - less chances of overlap later
