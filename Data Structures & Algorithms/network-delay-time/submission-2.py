from collections import defaultdict
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # OFFSET -1 goes to all node, k included
        distances = [float('inf')] * n
        distances[k - 1] = 0 # source
        graph = defaultdict(list)
        
        # build adjacency graph
        # -1 to offset 1..n
        for u, v, t in times:
            graph[u - 1].append((v - 1, t)) # store next node and weight


        min_heap = [(0, k - 1)] # distance to node and node itself (weight, node)
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            # opt here if
            if curr_dist > distances[node]:
                continue

            for nei, weight in graph[node]:
                # 2 choices - if sum weight > dinstances
                # that means we have reached this node for less time that what we currently can from this node
                dist = curr_dist + weight
                if dist < distances[nei]:
                    distances[nei] = dist
                    heapq.heappush(min_heap, (dist, nei))

        # if any inf left means we havent reached some nodes
        # print(distances)
        return max(distances) if max(distances) != float('inf') else -1    
        

        