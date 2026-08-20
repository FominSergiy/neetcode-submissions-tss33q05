from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda item: item[0])
        heap = []
        res = {}
        i = 0

        for q in sorted(queries):
            # add all intervals that start before or at query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r)) # (size, interval end)
                i += 1

            while heap and heap[0][1] < q: # remove any intervals that ended before the query
                heapq.heappop(heap)
            
            # at the end, our interval is either at the top of the heap or such interval does not exist
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]


