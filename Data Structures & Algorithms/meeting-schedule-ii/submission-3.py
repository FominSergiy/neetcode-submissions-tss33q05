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
        # process them in order and assign to room whenever room is available
        # can also use heap size to determine rooms needed
        intervals.sort(key = lambda item: item.start)
        
        # min heap with only ends stored
        heap = []
        rooms = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            # check if room is available
            if heap and start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
                continue
            
            # otherwise lets reserve new room
            heapq.heappush(heap, end)
            rooms += 1
        
        return rooms

        