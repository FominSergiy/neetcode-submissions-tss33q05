from collections import defaultdict
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float('inf')] * n
        distance[k - 1] = 0
        adj = [[] for _ in range(n)]

        for u, v, t in times:
            adj[u - 1].append((v - 1, t))
        
        heap = [(distance[k - 1], k - 1)]
        while heap:
            dist, node = heapq.heappop(heap)

            # at this dist we are already more than the existing value, can skip
            if dist > distance[node]:
                continue
            
            for nei, dist_to in adj[node]:
                total_dist = dist + dist_to
                if total_dist < distance[nei]:
                    distance[nei] = total_dist
                    heapq.heappush(heap, (total_dist, nei))
        
        ans = max(distance)
        # all nodes reached, shortest distance based on weight will be max in ans
        return ans if ans != float('inf') else - 1

  
        