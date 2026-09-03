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
        # intervals.sort(key=lambda interval: interval.start)
        # last_e = intervals[0].end

        # for interval in intervals[1:]:
        #     if last_e > interval.start:
        #         return False
        #     else:
        #         last_e = interval.end
        # return True


        # single - line sweep
        mp = defaultdict(int)
        for i in intervals:
            start, end = i.start, i.end
            mp[start] += 1
            mp[end] -= 1

        have = 0
        for i in sorted(mp):
            have += mp[i]
            if have > 1:
                return False
        return True

