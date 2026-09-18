"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # sorting and updating latest intervas
        # intervals.sort(key = lambda item: item.start)
        # last_e = intervals[0].end

        # for interval in intervals[1:]:
        #     start, end = interval.start, interval.end
        #     if last_e > start:
        #         return False
        #     last_e = end
        # return True
        



        # single - line sweep
        mp = defaultdict(int)
        for interval in intervals:
            start, end = interval.start, interval.end
            mp[start] += 1
            mp[end] -= 1
        

        have = 0
        for key in sorted(mp):
            have += mp[key]
            if have > 1:
                return False
        return True



