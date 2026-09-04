from heapq import *
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda interval: interval[0])
        heap = []
        i = 0
        mp = {}


        # single query may have multiple intervals to which it could belong
        # for query, as long as query >= start -> belongs here
        # converserly, for the qeury, it does not belog when end > query

        # which means we can, for each query in asc order
        # 1. find all intervals it belongs to
        # 2. remove all intervals it does not
        # 3. if heap remains, top is our num else -1
        for query in sorted(queries):
            while i < len(intervals) and query >= intervals[i][0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            # filter ones are not matching
            # at this point we only want to drop older intervals
            # behind the query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            mp[query] =  heap[0][0] if heap else -1
        
        return [mp[q] for q in queries]

