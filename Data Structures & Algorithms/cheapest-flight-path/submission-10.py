from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # still track elements in heap based on price
        # but use stops as weights
        # before stepping into adj nodes, check for stops
        stops = [float('inf')] * n
        stops[src] = 0 # starting point starts at 0
        adj = [[] for _ in range(n)]

        for u, v, p in flights:
            adj[u].append((v, p))
        
        heap = [(0, src, 0)] # cost, node, stops
        while heap:
            cost, node, step = heapq.heappop(heap)

            if step > k + 1 or step > stops[node]:
                continue
            
            if node == dst:
                return cost
            
            stops[node] = step
            for nei, nei_c in adj[node]:
                heapq.heappush(heap, (nei_c + cost, nei, step + 1))

        return -1