class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: (item[0]));
        prev_end = intervals[0][1]
        remove = 0

        # greedy local choices
        # 1 - for interval[i] if  no overlap with previous end
        # set prev end to this end

        # 2. otherwise there is overlap
        # keep the shorter interval - less chances of overlap later
        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                remove += 1
                prev_end = min(prev_end, end)
        
        return remove
        