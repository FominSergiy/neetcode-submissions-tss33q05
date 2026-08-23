"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # sorting and updating latest interval
        intervals.sort(key = lambda item: item.start)
        last_e = intervals[0].end

        for interval in intervals[1:]:
            if last_e > interval.start:
                return False
            last_e = interval.end
        return True


        # single - line sweep