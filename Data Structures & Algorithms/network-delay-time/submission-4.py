from collections import defaultdict
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # weights is what helps us pick the right path
        # works with min heap by taking the smallest path
        distances = [float('inf')] * n
        distances[k - 1] = 0
        graph = defaultdict(list)
        
        # build directed graph
        for u, v, t in times:
            graph[u - 1].append((v - 1, t))
        
        heap = [(0, k - 1)] # time, edge
        while heap:
            steps_so_far, node = heapq.heappop(heap)

            # steps greater than steps at current node
            if steps_so_far > distances[node]:
                continue
            
            for nei, steps_to_nei in graph[node]:
                # this path has weight greater than existing, skip
                total_steps = steps_so_far + steps_to_nei
                if total_steps >= distances[nei]:
                    continue

                distances[nei] = total_steps
                heapq.heappush(heap, (total_steps, nei))
        
        ans = max(distances)
        return ans if ans != float('inf') else -1
 
        