"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        min_heap = [] # end time when available
        rooms = 0

        for interval in intervals:
            # first check if there are any rooms available
            # resume if available
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval.end)
                continue
            
            # if not, get a new room
            rooms += 1
            heapq.heappush(min_heap, interval.end)
        
        return rooms

        