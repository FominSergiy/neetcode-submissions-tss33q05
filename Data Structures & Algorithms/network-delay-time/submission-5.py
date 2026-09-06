from collections import defaultdict
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # weights is what helps us pick the right path
        # works with min heap by taking the smallest path
        distance = [float('inf')] * n
        distance[k - 1] = 0 # set distance for source node to be 0
        graph = defaultdict(list)
        
        for u, v, t in times:
            graph[u - 1].append((v - 1, t)) # node and time it takes
        
        heap = [(0, k - 1)]
        while heap:
            dst, node = heapq.heappop(heap)

            # if at this node current time is greater than the
            # recorded - we can skip
            if dst > distance[node]:
                continue
            
            # we only want to move into nodes where
            # distance is less!
            for nei, dst_to_nei in graph[node]:
                total_dist = dst + dst_to_nei
                if total_dist < distance[nei]:
                    distance[nei] = total_dist
                    heapq.heappush(heap, (total_dist, nei))
        
        # ans should be highest int in distances
        # unless it inf - meaning we havent reached that node
        # print(distance)
        ans = max(distance)
        return ans if ans != float('inf') else -1


  
        