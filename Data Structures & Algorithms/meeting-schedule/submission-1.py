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
        # iterate over meetings, if any conficts return false
        intervals.sort(key=lambda x: x.start)
        last_e = intervals[0].end

        for interval in intervals[1:]:
            if last_e <= interval.start:
                last_e = interval.end
            else:
                return False
        return True
