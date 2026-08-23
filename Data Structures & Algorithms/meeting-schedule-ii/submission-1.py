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
        # use heap to keep track of most recent available rooms
        # and only provision new rooms when no existing available
        intervals.sort(key=lambda x: x.start)
        heap = []
        need_rooms = 0

        for interval in intervals:
            start, end = interval.start, interval.end

            # check if we can occupy any existing rooms
            if heap and start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
                continue
            
            # otherwise all rooms occupied and we need another room
            heapq.heappush(heap, end)
            need_rooms += 1
        
        return need_rooms
        