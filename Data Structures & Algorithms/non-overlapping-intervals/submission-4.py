class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # scan in sorted list from smallest to largest
        # any time there is a conflict, pick smallest end - meaning we take out largest interval that will cause more removals
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
