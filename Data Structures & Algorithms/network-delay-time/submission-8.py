from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float('inf')] * n
        distance[k - 1] = 0

        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))
        
        heap = [(distance[k - 1], k - 1)] # (dist, source)

        while heap:
            dist, node = heapq.heappop(heap)

            if dist > distance[node]:
                continue
            
            for nei, nei_dist in adj[node]:
                total_dist = dist + nei_dist
                if total_dist < distance[nei]:
                    distance[nei] = total_dist
                    heapq.heappush(heap, (total_dist, nei))
        
        ans = max(distance)
        return ans if ans != float('inf') else -1

  
        