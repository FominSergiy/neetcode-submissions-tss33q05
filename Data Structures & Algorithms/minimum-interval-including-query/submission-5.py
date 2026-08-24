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
            while i < len(intervals) and query >= intervals[i][0]:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            
            while heap and query > heap[0][1]:
                heapq.heappop(heap)
            
            res[query] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]

