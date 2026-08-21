from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda item: item[0])
        heap = [] # (size, end)
        res = {}
        i = 0


        # single query may have multiple intervals to which it could belong
        # for query, as long as query >= start -> belongs here
        # converserly, for the qeury, it does not belog when end > query

        # which means we can, for each query in asc order
        # 1. find all intervals it belongs to
        # 2. remove all intervals it does not
        # 3. if heap remains, top is our num else -1
        for query in sorted(queries):
            # find belong intervals
            while i < len(intervals) and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            # does not belong - for the heap
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            res[query] = heap[0][0] if heap else -1


        return [res[q] for q in queries]


